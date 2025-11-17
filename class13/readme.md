# Class 13: What the hell is R? / Deconstructing stories

[What the hell is R?](https://prezi.com/hsbuuq7r3z1n/what-the-hell-is-r/)

## What else is out there

* IRE/NICAR
* NICAR conference (next March in Indianapolis)
* News Nerdery slack 
* Books
    * The Wall Street Journal Guide to Information Graphics
    * How Charts Lie: Getting Smarter about Visual Information
    * Numbers In The Newsroom

## Department of Data Reconstruction

Recreate the following visualizations in this piece: https://www.washingtonpost.com/business/2023/10/27/native-americans-2020-census/

Turn in links to your charts as `EC-WaPo.md` for extra credit. Feel free to ask AI for help with the data cleaning. 

* Slighly muddled counts of Native American origins (1 extra credit point)
    * Hints:
        * Use rows that say "alone" for the "single-origin" column
        * Use rows that say "combo" for the "All" column
        * You'll need to make a pivot table to format the data for the graphic
        * You'll need to exclude some rows 
        * You can turn on "search" function in Datawrapper for a table

* Native American Origins, 2020 (*only the Cherokee map*) (2 extra credit points)
    * Hints: 
        * You'll only use rows labeled `Cherokee alone or in any combination` (POPGROUP 2908)
        * You may need to "transpose" the total population file 
        * You'll need to merge the total population and Cherokee population data, using a lookup on the county name columns
        * Once you do the merge, you can calculate the pct of Cherokee per county population
        * In Datawrapper, you'll use the GEO_ID column as your FIPS code. BUT you only want to include the last five digits (everything after `0500000US`).
        * Do your best with the custom color steps to match the WAPO graphic, but no need to get it perfect


### Data sources

* Detailed table of tribes for whole nation 
    * [tribe-alone-combo.csv](tribe-alone-combo.csv)
    * Originally from: https://data.census.gov/table/DECENNIALDDHCA2020.T01001?t=-08&g=010XX00US&d=DEC+Detailed+Demographic+and+Housing+Characteristics+File+A 

* Detailed table of tribes by county 
    * https://data.census.gov/table/DECENNIALDDHCA2020.T01001?t=-08&g=010XX00US$0500000&d=DEC+Detailed+Demographic+and+Housing+Characteristics+File+A

* Total population by county
    * https://data.census.gov/table/DECENNIALDHC2020.P1?q=county+population+2020&d=DEC+Demographic+and+Housing+Characteristics