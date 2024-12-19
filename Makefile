abxy.duckdb:
	duckdb abxy.duckdb -init abxy.sql -no-stdin

clean:
	rm -f abxy.duckdb
