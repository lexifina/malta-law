"""Print a Maltese law, or one article of it, as it stood on a date.

    python tools/in_force_on.py 2022-06-01 cap/12          # every file of Cap. 12 on that day
    python tools/in_force_on.py 2022-06-01 cap/12 57       # article 57
    python tools/in_force_on.py 2022-06-01 sl/12.36        # a piece of subsidiary legislation

Reads the `In-force:` and `Consolidated:` trailers (the real dates; commit dates before 1970 are clamped), so it is
right for any day, and the order of commits does not matter. Then applies the correction commits (`Kind: correction`):
each sets the files its `Files:` trailers name to the text in its own tree, on the days of its `Corrects:` range. An
open range (`<from>..`) ends the day before the law's next ordinary commit. Standard library only.
"""
import subprocess
import sys
from datetime import date, timedelta

FS, RS = '\x1f', '\x1e'


def git(*args: str) -> str:
    return subprocess.run(['git', '-c', 'core.quotePath=false', *args], capture_output=True, text=True,
                          encoding='utf-8', check=True).stdout


def ordinary(law: str) -> list[tuple[int, str, str]]:
    """(history position, commit, day) of every commit that touches the law and is not a correction."""
    fmt = (f'%H{FS}%(trailers:key=Kind,valueonly,separator=)' f'{FS}%(trailers:key=In-force,valueonly,separator=)'
           f'{FS}%(trailers:key=Consolidated,valueonly,separator=){RS}')
    out = []
    for i, rec in enumerate(git('log', '--reverse', '--first-parent', f'--format={fmt}', 'main', '--', f'{law}/').split(RS)):
        parts = rec.strip('\n').split(FS)
        if len(parts) < 4 or parts[1].strip() == 'correction':
            continue
        d = (parts[2] or parts[3]).strip()[:10]
        if d:
            out.append((i, parts[0], d))
    return out


def corrections(law: str) -> list[dict]:
    """The correction commits for the law, in history order: {commit, from, to or None, files}."""
    fmt = (f'%H{FS}%(trailers:key=Kind,valueonly,separator=)' f'{FS}%(trailers:key=Corrects,valueonly,separator=%x1d)'
           f'{FS}%(trailers:key=Files,valueonly,separator=%x1d){RS}')
    out = []
    for rec in git('log', '--reverse', '--first-parent', '--grep=^Kind: correction', f'--format={fmt}', 'main').split(RS):
        parts = rec.strip('\n').split(FS)
        if len(parts) < 4 or parts[1].strip() != 'correction':
            continue
        for c in parts[2].split('\x1d'):
            name, _, span = c.strip().partition(' ')
            if name.strip('/') != law or '..' not in span:
                continue
            a, _, b = span.strip().partition('..')
            files = [f.strip() for f in parts[3].split('\x1d') if f.strip().startswith(law + '/')]
            out.append({'commit': parts[0], 'from': a, 'to': b or None, 'files': files})
    return out


def day_before(day: str) -> str:
    return (date.fromisoformat(day) - timedelta(days=1)).isoformat()


def files_on(day: str, law: str) -> dict[str, tuple[str, str]]:
    """path -> (commit, path) whose blob holds the text in force on `day`."""
    rows = ordinary(law)
    best = None
    for i, h, d in rows:  # the greatest in-force day on or before `day`; a later commit wins a tie
        if d <= day and (best is None or d >= best[2]):
            best = (i, h, d)
    out = {}
    if best:
        for n in git('ls-tree', '-r', '--name-only', best[1], f'{law}/').split('\n'):
            if n.endswith('.md'):
                out[n] = (best[1], n)
    for c in corrections(law):
        end = c['to'] or day_before(min((d for _, _, d in rows if d > c['from']), default='9999-12-31'))
        if not (c['from'] <= day <= end):
            continue
        have = set(git('ls-tree', '-r', '--name-only', c['commit'], f'{law}/').split('\n'))
        for f in c['files']:
            if f in have:
                out[f] = (c['commit'], f)
            else:
                out.pop(f, None)
    return out


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, law = sys.argv[1], sys.argv[2].strip('/')
    unit = sys.argv[3] if len(sys.argv) > 3 else None
    files = files_on(day, law)
    if unit:
        path = f'{law}/{unit}.md'
        if path not in files:
            sys.exit(f'{path}: no version on or before {day} (the record starts at the first consolidated version)')
        h, p = files[path]
        sys.stdout.write(git('show', f'{h}:{p}'))
        return
    if not files:
        sys.exit(f'{law}: no version on or before {day} (the record starts at the first consolidated version)')

    def order(n: str):
        stem = n.rsplit('/', 1)[-1][:-3]
        num = ''.join(c for c in stem if c.isdigit())
        return (stem != 'title', not stem[:1].isdigit(), int(num) if num and stem[:1].isdigit() else 0, stem)
    for n in sorted(files, key=order):
        h, p = files[n]
        sys.stdout.write(git('show', f'{h}:{p}') + '\n')


if __name__ == '__main__':
    main()
