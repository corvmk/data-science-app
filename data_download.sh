#!/bin/bash

if [ -z "$1" ]; then
    echo "Start year not set, defaulting to 2019"
    START_YEAR=2019
else
    START_YEAR=$1
fi

if [ -z "$2" ]; then
    echo "End year not set, defaulting to start year"
    END_YEAR=$START_YEAR
else
    END_YEAR=$2
fi

if [ $START_YEAR -gt $END_YEAR ]; then
    echo "ERROR: End year is lower than start year"
    exit 1
fi

for year in $(seq $START_YEAR $END_YEAR)
do
    for m in {01..12}
    do
        wget -P data https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_$year-$m.parquet
    done
done
