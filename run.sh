#!/usr/bin/env bash
set -euo pipefail

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$script_dir"

basedpyright #Better than pyright
uv run main.py --base '~suraaj' #TODO: Don't hardcode this

if [[ -n "${sync_cornell:-}" ]]; then #Because I did set -u
  rsync -av '_dist/~suraaj/' coecis:/people/sk2727/
else
  uv run python -m http.server -d _dist
fi

