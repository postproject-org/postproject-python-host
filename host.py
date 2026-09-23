"""Disposable Python host experiment for PostProject's installed ABI package."""

import argparse
import json
from pathlib import Path

from postproject import Production


def exercise(production_path: Path, media_path: Path, library_path: Path) -> dict:
    with Production.create(
        production_path, "Python host spike", library_path=library_path
    ) as production:
        with production.transaction(origin="org.postproject.spike.python") as transaction:
            asset_id = transaction.import_media(media_path, "Host clip")
        representation = production.representations[asset_id][0]
        reference = production.host_bindings[representation.id]
        resolution = production.resolve(asset_id)[0]
        return {
            "asset_id": str(asset_id),
            "reference": reference,
            "availability": resolution.availability.value,
            "representations": len(production.representations[asset_id]),
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("production", type=Path)
    parser.add_argument("media", type=Path)
    parser.add_argument("--library", type=Path, required=True)
    arguments = parser.parse_args()
    print(json.dumps(exercise(arguments.production, arguments.media, arguments.library)))


if __name__ == "__main__":
    main()

