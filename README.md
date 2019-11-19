# gdcdata cost - accuracy analysis  
In its current state, this github repo provides a comprehensive analysis on variant calling
data from the Genomic Data Commons.    
  
Files comb.py, df.py, howmany.py, inter.py, contents.py contain the necessary libraries of 
functions for the analysis. 

gdc.ipynb contains all the necessary code for plotting upset plots and venn diagrams of the 
data, with or without filtering.   

gdc_stats.ipynb provides a stack bar plot visualization of the average proportion of variants(unfiltered)
that each combination of variant callers found for each patient from the gdc data. 

function.ipynb contains a function for useful tables for accuracy analysis, as well as a function that performs outlier analysis for the largest outlier (most number of variants) of the patients. 

meta_model.ipynb contains random forest models to predict whether an additional variant caller will yield any increase in accuracy given a set of baseline callers and the features from the model_pkl_files extracted from the MAF files. 

There are three available filtering methods: pairing genes with corresponding cancers from the Bailey_et_al_2018_sig_mut_genes.txt
file, taking the list of genes from the Cancer_Gene_Census_all_Jun-11-2019.csv file, or filtering via the list of PANCAN 
genes from the Bailey file. 

