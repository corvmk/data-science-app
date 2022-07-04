""""
NOT WORKING!!! TODO
"""


from tempfile import TemporaryDirectory
import pandas as pd
from sqlalchemy import create_engine
import subprocess
from pathlib import Path
from tqdm import tqdm
import os


def download_yellow_cab_data():
    subprocess.run(["./data_download.sh", "2019", "2019"])


def pq_to_csv(data_files: list[Path], target_folder: Path = Path("csv_data")):
    target_folder.mkdir(exist_ok=True)
    for x in tqdm(data_files):
        target_file_name = x.stem + ".csv"
        df = pd.read_parquet(x)
        df.to_csv(target_folder / target_file_name, sep="|", decimal=".")
        # delete trailing newline - stupid problem
        # print("Truncating file")
        # with open(target_folder / target_file_name, "w") as file:
        #     file.seek(-2, os.SEEK_END)
        #     file.truncate()


def create_table(data_files: list[Path], table_name: str = "yellow_taxi"):
    """Create table for yellow taxi storage

    Parameters
    ----------
    data_files : list[Path]
        _description_
    """
    engine = create_engine("postgresql://postgres:postgres@postgres")
    with engine.connect() as conn:
        conn.execute("DROP TABLE IF EXISTS yellow_taxi")
        pd.read_parquet(data_files[0]).head(0).to_sql(
            name=table_name, con=conn, if_exists="replace"
        )
    return table_name


download_path = Path()


def main():
    """Main runner for feeding Postgres"""
    # download_yellow_cab_data()
    data_files = [x for x in Path("data").iterdir() if x.suffix == ".parquet"]
    pq_to_csv(data_files[:1])
    # remove last newline


if __name__ == "__main__":
    main()
