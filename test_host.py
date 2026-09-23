import os
from pathlib import Path

from host import exercise


def test_python_host_round_trip(tmp_path):
    media = tmp_path / "clip.mov"
    media.write_bytes(b"python host media")
    result = exercise(
        tmp_path / "host.pproj", media, Path(os.environ["POSTPROJECT_LIBRARY"])
    )
    assert result["availability"] == "online"
    assert result["representations"] == 1
    assert result["reference"].startswith("https://postproject.org/ref/v1/")

