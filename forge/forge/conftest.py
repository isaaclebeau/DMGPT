import uuid
from pathlib import Path

import pytest

from forge.file_storage.base import FileStorage, FileStorageConfiguration
from forge.file_storage.local import LocalFileStorage


@pytest.fixture()
def tmp_project_root(tmp_path: Path) -> Path:
    return tmp_path


@pytest.fixture()
def app_data_dir(tmp_project_root: Path) -> Path:
    dir = tmp_project_root / "data"
    dir.mkdir(parents=True, exist_ok=True)
    return dir


@pytest.fixture()
def storage(app_data_dir: Path) -> FileStorage:
    storage = LocalFileStorage(
        FileStorageConfiguration(
            root=Path(f"{app_data_dir}/{str(uuid.uuid4())}"), restrict_to_root=False
        )
    )
    storage.initialize()
    return storage
