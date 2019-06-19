from contents import set_contents
import pandas as pd
import os
from comb import parse_maf
from howmany import how_many_tumor, how_many_tumor_cgc, how_many_pancan
import numpy as np

def baileydf(possible_cancers, possible_callers, keys, original, impacts, filt):
    g = np.array(np.genfromtxt('Bailey_et_al_2018_sig_mut_genes.txt',dtype=None,encoding = None, usecols = (0)))
    c = np.genfromtxt('Bailey_et_al_2018_sig_mut_genes.txt',dtype=None,encoding = None, usecols = (1))
    genes = np.delete(g,4)
    cancers = np.delete(c,4)
    dictofgenes = dict([(cancer, set()) for cancer in cancers])

    for i in range(len(genes)):
        dictofgenes[cancers[i]].add(genes[i])

    pancandict = dictofgenes['PANCAN']
    coadread = dictofgenes['COADREAD']

    del dictofgenes['PANCAN']
    del dictofgenes['COADREAD']

    dfbailey = pd.DataFrame(0, index=keys, columns=possible_cancers)

    for cancer in possible_cancers:
        os.chdir(original)
        os.chdir(cancer)
        mafs = os.listdir()

        maf_fps = {}
        for caller in possible_callers:
            for maf in mafs:
                if caller in maf: # str in the filepath
                    maf_fps[caller] = maf

        all_variants = {}
    
        for caller in maf_fps:
            all_variants[caller] = parse_maf(maf_fps[caller])
        arg = []
        for i in range(len(possible_callers)):
            arg.append(all_variants[possible_callers[i]])

        content = set_contents(arg, possible_callers, keys)
        dfbailey.loc[:,cancer] = how_many_tumor(cancer, coadread, content, dictofgenes, filt, impacts, keys)
    os.chdir(original)
    return dfbailey

def cgcdf(possible_cancers, possible_callers, keys, original, impacts, filt):
    os.chdir(original)
    cgc = pd.read_csv('Cancer_Gene_Census_all_Jun-11-2019.csv', usecols = (0,9))
    dfcgc = pd.DataFrame(np.nan, index=keys, columns=possible_cancers)

    for cancer in possible_cancers:
        os.chdir(original)
        os.chdir(cancer)
        mafs = os.listdir()

        maf_fps = {}
        for caller in possible_callers:
            for maf in mafs:
                if caller in maf: # str in the filepath
                    maf_fps[caller] = maf

        all_variants = {}
    
        for caller in maf_fps:
            all_variants[caller] = parse_maf(maf_fps[caller])
        
        arg = []
        for i in range(len(possible_callers)):
            arg.append(all_variants[possible_callers[i]])
            
        content = set_contents(arg, possible_callers, keys)
        dfcgc.loc[:,cancer] = how_many_tumor_cgc(content, cgc, filt, impacts, keys)
    os.chdir(original)   
    return dfcgc

def pancandf(possible_cancers, possible_callers, keys, original, impacts, filt):
    g = np.array(np.genfromtxt('Bailey_et_al_2018_sig_mut_genes.txt',dtype=None,encoding = None, usecols = (0)))
    c = np.genfromtxt('Bailey_et_al_2018_sig_mut_genes.txt',dtype=None,encoding = None, usecols = (1))
    genes = np.delete(g,4)
    cancers = np.delete(c,4)
    dictofgenes = dict([(cancer, set()) for cancer in cancers])

    for i in range(len(genes)):
        dictofgenes[cancers[i]].add(genes[i])

    pancandict = dictofgenes['PANCAN']
    
    dfpancan = pd.DataFrame(np.nan, index=keys, columns=possible_cancers)

    for cancer in possible_cancers:
        os.chdir(original)
        os.chdir(cancer)
        mafs = os.listdir()

        maf_fps = {}
        for caller in possible_callers:
            for maf in mafs:
                if caller in maf: # str in the filepath
                    maf_fps[caller] = maf

        all_variants = {}
    
        for caller in maf_fps:
            all_variants[caller] = parse_maf(maf_fps[caller])
        arg = []
        for i in range(len(possible_callers)):
            arg.append(all_variants[possible_callers[i]])
            
        content = set_contents(arg, possible_callers, keys)    
        dfpancan.loc[:,cancer] = how_many_pancan(content, pancandict, filt, impacts, keys)
    os.chdir(original)    
    return dfpancan