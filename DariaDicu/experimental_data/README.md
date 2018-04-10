# Raw data files and metadata

## 2-3-17.txt, 10-3-17.txt, 16-12-16.txt

Raw data collected on 3 separate days. Extracted using software from here
https://www.thermofisher.com/at/en/home/technical-resources/software-downloads/applied-biosystems-7900ht-fast-real-timespcr-system.html

Columns denoted with a ".1" are background-corrected

## *.xlsx

- Contain metadata for qPCR runs
- The "Well" column converts a 384 well plate coordinate (e.g. K7) to an integer (e.g. 247). If the row is an integer r = 0,...,15 and the column an integer c = 0,...,23 then Well=24*r+c+1.

### `BJ-2-3-2017-sortedsinglecellHBplate6-16SA.xlsx` (sheet `BJ-2-3-2017-sortedsinglecellHBp`)

- The column "Sample Name" contains a description of what the corresponding well contained.
	-  BG plate 9 0 cells row 7 c 1 : Well contained 0 cells
	- BG plate 9 10 cells row 7 c 7 : Well contained 10 cells
	- BG plate 9 sing cells row 1 c 1 : Well contained 1 cell
	- CO2 PCR product 1000 0000 1:10 s : A DNA standard for the COII gene, factors of x10 dilution from 10^6 copies of DNA
- The column "Detector Name" denotes the primer used to 
	- BJ-CYB C57 vs BGHBST : TO BE CONFIRMED, primer against CyB?
	- BJCOII : Primer against COII

### `BJ-10-3-2017-STsortedcells-MUPSTDdiff.xlsx` (sheet `BJ-10-3-2017-STsortedcells-MUPS`)

- qPCR against the MUP gene
- Similar naming conventions to `BJ-2-3-2017-sortedsinglecellHBplate6-16SA.xlsx`
- "MUP STD Qiagen" under "Sample Name" denotes a DNA standard against MUP

### `BJ-16-12-2016-sortedcellsAndtestMUP.xlsx` (sheet `BJ-16-12-2016-sortedcellsAndtestMUP.xlsx`)

- Similar to `BJ-10-3-2017-STsortedcells-MUPSTDdiff.xlsx`

## `Explore_Raw_Data.ipynb`

- A Jupyter Notebook to open and look at the data, for debugging





