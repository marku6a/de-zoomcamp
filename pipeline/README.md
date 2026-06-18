Start Postgres database in Docker:
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18

Connect pgcli to the db:
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi

Run ingestion command:
uv run python ingest_data.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=localhost \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=yellow_taxi_trips_2021_01 \
  --year=2021 \
  --month=01 \
  --chunksize=100000