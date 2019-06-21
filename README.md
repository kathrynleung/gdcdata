# gdcdata cost - accuracy analysis  
In its current state, this github repo provides a comprehensive analysis on variant calling
data from the Genomic Data Commons.    
  
Files comb.py, df.py, howmany.py, inter.py, contents.py contain the necessary libraries of 
functions for the analysis. (These libraries are still a work in progress)

See the plots folder for upset plots of the GDC data without any filtering. 

gdc.ipynb contains all the necessary code for plotting upset plots and venn diagrams of the 
data, with or without filtering.   

gdc_stats.ipynb provides a stack bar plot visualization of the average proportion of variants(unfiltered)
that each combination of variant callers found for each patient from the gdc data. 

function.ipynb contains a function for useful tables for accuracy analysis, as well as a function that performs outlier analysis for the largest outlier(most number of variants) of the patients. 


There are three available filtering methods: pairing genes with correpsonding cancers from the Bailey_et_al_2018_sig_mut_genes.txt
file, taking the list of genes from the Cancer_Gene_Census_all_Jun-11-2019.csv file, or filtering via the list of PANCAN 
genes from the Bailey file. 

Please note: this repo is a work on progress. Work is currently being done to optimize the functions/data parsing, organize
and modularize the code to make it more user friendly. 

