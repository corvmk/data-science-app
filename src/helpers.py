"""
Functions for queueing
"""
from time import sleep
from random import randint
import pandas as pd
from sqlalchemy import create_engine


def get_sql(day):
    """
    Helper for generating the necessary sql
    """
    sql = f"""
    SELECT tpep_pickup_datetime,
    passenger_count, trip_distance, fare_amount FROM yellow_taxi
    WHERE TO_CHAR(tpep_pickup_datetime, 'yyyy-mm-dd') = '{day}'
    """
    return sql


def get_dataframe(day, con_str, target_loc):
    """
    Worker function for getting the data
    """
    sleep(randint(1, 15))
    engine = create_engine(con_str)
    with engine.connect() as con:

        df = pd.read_sql(get_sql(day), con)
        df.to_parquet(target_loc/f"yellow_taxi-{day}.parquet")
    return {"day": day, "size": len(df)}
