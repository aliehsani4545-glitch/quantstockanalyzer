import zipfile
import os
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
OUTPUT_ZIP = PROJECT_DIR.parent / "quantstockanalyzer.zip"
EXCLUDE = {".git", "__pycache__", ".mypy_cache", ".pytest_cache", "quantstockanalyzer.zip"}


def should_exclude(path: Path) -> bool:
    return any(part in EXCLUDE for part in path.parts)


def zip_project():
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in PROJECT_DIR.rglob("*"):
            if file.is_file() and not should_exclude(file.relative_to(PROJECT_DIR)):
                arcname = Path("quantstockanalyzer") / file.relative_to(PROJECT_DIR)
                zf.write(file, arcname)
                print(f"  Added: {arcname}")

    size_kb = OUTPUT_ZIP.stat().st_size / 1024
    print(f"\nDone! {OUTPUT_ZIP} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    zip_project()
