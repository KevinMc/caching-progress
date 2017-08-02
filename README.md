# caching-progress

1. Using GSAK, go to `File > Backup…` and select the database you want to map. GSAK will export a zipped file.
2. From the zip file contents, locate the `sqlite.db3` file 
3. Run `counties_by_year.py` from the same folder as the database file. You will also need `counties-fips.csv` (originally [obtained from the U.S. Census](https://www.census.gov/geo/reference/codes/cou.html)). This file uses the `difflib` Python library to match county names, which are not identical between the Census and GSAK input. The output of this script can be saved as `caching.tsv`.
4. `county_data.json` is an output of `counties-all.py`. It outputs a list of caches, each with the geocaching.com log ID, code, name, county, state, and date found .

To generate the map, the `index.html` needs to reference the two data files for coloring and also a GeoJSON file for map rendering. `us.json` is such a file for United States counties, where each's features `id` is the FIPS code listed in `caching.tsv`.
