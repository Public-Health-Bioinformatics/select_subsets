# select_subsets

This Galaxy tool enables a user to create separate dataset(s) of selections user has made from a tabular dataset.  A separate dataset is created for each group of selected items indicated by 2nd-last column (a group key).  Last column must be a unique incremented id for each row.

Produced by https://github.com/Public-Health-Bioinformatics

## Usage

Before using this tool, ensure the source tabular dataset has:

	1) Incremented row number in last column.  You can use the tool **Add column to an existing dataset (Text Manipulation)** 
	with the parameters **Add this value: 1** and **Iterate?: YES**.  
	2) 2nd last column controls grouping:  If you want the tool to divide up your data into separate datasets of selections, include a short Grouping key (&lt;10 chars) in this column.  If no grouping desired, leave this column empty. 

## Usage in conjunction with Blast Reporting tool

This tool can be used in conjunction with the BLAST Reporting tool's "Selectable HTML Report".  When that report is selected, the tool also produces a "Sequence Selection List" of queries and hits, which contains the necessary grouping and row index fields described below.  The HTML Report can directly submit selections to the Select Subsets tool for processing.  That functionality requires Galaxy administrator setup.

## Installation

The Galaxy tool can be installed from https://toolshed.g2.bx.psu.edu/ .

