Connect pgcli to the db:
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi

Run docker ingest:
docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v001 \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=yellow_taxi_trips_2021_01 \
  --year=2021 \
  --month=01 \
  --chunksize=100000