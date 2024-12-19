abxy.xlsx: abxy.duckdb
	python abxy.py

abxy.duckdb:
	duckdb abxy.duckdb -init abxy.sql -no-stdin

clean:
	rm -f abxy.duckdb abxy.xlsx
