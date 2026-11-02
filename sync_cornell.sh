#!/usr/bin/env bash
set -euo pipefail

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$script_dir"

uv run pyright
uv run main.py --base '~suraaj'
rsync -av '_dist/~suraaj/' coecis:/people/sk2727/
