#!/usr/bin/env bash
set -e

script_dir="$( cd "$( dirname "$(realpath "${BASH_SOURCE[0]}")" )" >/dev/null 2>&1 && pwd )"
cd "$script_dir"

uv run pyright
uv run build_site.py
