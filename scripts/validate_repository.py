#!/usr/bin/env python3
"""Validate the collection layout without assembling DOS-targeted programs."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRAMS = (
    "strings/palindrome",
    "strings/case-insensitive-matching",
    "numbers/perfect-number",
    "numbers/prime-and-sequences",
    "matrices/multiplication",
    "system/current-time",
    "graphics/checker-board",
)
GENERATED_SUFFIXES = {".com", ".exe", ".ilk", ".lst", ".map", ".obj", ".pdb"}


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files"], cwd=ROOT, text=True
    )
    return [ROOT / line for line in output.splitlines()]


def validate_layout(errors: list[str]) -> None:
    for relative in PROGRAMS:
        program = ROOT / relative
        for required in (program / "README.md", program / "src" / "main.ASM"):
            if not required.is_file():
                errors.append(f"missing required file: {required.relative_to(ROOT)}")


def validate_generated_files(errors: list[str]) -> None:
    for path in tracked_files():
        if path.suffix.lower() in GENERATED_SUFFIXES:
            errors.append(f"generated artifact is tracked: {path.relative_to(ROOT)}")


def validate_readme_images(errors: list[str]) -> None:
    image_pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE)
    for relative in PROGRAMS:
        readme = ROOT / relative / "README.md"
        for image in image_pattern.findall(readme.read_text(encoding="utf-8")):
            if image.startswith(("http://", "https://")):
                errors.append(f"external image URL in {readme.relative_to(ROOT)}: {image}")
                continue
            if not (readme.parent / image).is_file():
                errors.append(f"broken image in {readme.relative_to(ROOT)}: {image}")


def main() -> int:
    errors: list[str] = []
    validate_layout(errors)
    validate_generated_files(errors)
    validate_readme_images(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(PROGRAMS)} assembly programs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
