import os
from pathlib import Path

from util import convert_tokenized_to_conll

DATASET_ENV = {
    "JP-5": "SHINRA2020JP5",
    "Organization":"SHINRA2020ORGANIZATION",
    "Location":"SHINRA2020LOCATION",
    "Event":"SHINRA2020EVENT",
    "Facility":"SHINRA2020FACILITY",
}

DATASET_DIR = {c_cls:os.environ.get(env)
    for c_cls, env in DATASET_ENV.items() if os.environ.get(env) is not None}
assert len(DATASET_DIR) != 0, f"次の環境変数の1つ以上にデータセットのパスを格納する必要があります。\n{list(DATASET_ENV.values())}"

if __name__ == "__main__":
    for c_cls, data_dir in DATASET_DIR.items():
        data_dir = Path(data_dir)
        for path in data_dir.glob('*'):
            print(path)
            convert_tokenized_to_conll(path)


