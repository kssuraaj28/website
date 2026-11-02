import shutil
from cur_dir import ROOT
from paths import SitePath

DISTOUT = ROOT / "_dist"
ASSETS = ROOT / 'assets' # TODO: This should be somewhere else

def clean_dist():
    # Start from an empty output directory, so that no stale files get deployed.
    shutil.rmtree(DISTOUT, ignore_errors=True)
    DISTOUT.mkdir()


def install_dist(base: SitePath, index_html: str):
    site_root = DISTOUT.joinpath(*base.content)
    site_root.mkdir(parents=True, exist_ok=True)
    path = site_root / "index.html"
    path.write_text(index_html, encoding='utf-8')
    shutil.copytree(ASSETS, site_root / ASSETS.name)
