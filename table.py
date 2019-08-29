import pandas as pd
from df import baileydf, cgcdf, pancandf
from comb import my_combs_all
from tabulate import tabulate
import numpy as np
def table(callers, additional_callers, cancer, cardinality, impacts, filt, keys, bcp, individual, tab):

    if isinstance(bcp, pd.DataFrame):
        if 'Total' in bcp.index:
            df = bcp.drop(['Total'], axis=0)
        else:
            df = bcp
    elif bcp == 'BAILEY':
        df = baileydf(possible_cancers, possible_callers, keys,impacts, filt).drop(['Total'], axis=0)
    elif bcp == 'CGC':
        df = cgcdf(possible_cancers, possible_callers, keys, impacts, filt).drop(['Total'], axis=0)
    elif bcp == 'PANCAN':
        df = pancandf(possible_cancers, possible_callers, keys, impacts, filt).drop(['Total'], axis=0)
    
    
    sets = []
    if len(callers) >= 1:
        sets.append(list(callers))
    ad = my_combs_all(additional_callers, len(additional_callers))

    for n in range(len(ad)):
        sets.append(callers+list(ad[n]))

    for i in range(len(sets)):
        sets[i] = tuple(sets[i])
    
    #if len(callers) >= cardinality:
    sums = pd.DataFrame(0, index=sets, columns=('real', 'real % diff', 'total', 'total % diff', '% of all real'))
    #else:
    #    sums = pd.DataFrame(0, index=sets, columns=('real', 'total', '% of all real'))
    
    # real counts
    su = []
    for i in range(len(sets)):
        index = []
        for j in range(len(keys)):
            if len(set(sets[i])&keys[j]) >= 1 and len(keys[j]) >= cardinality:
                index.append(j)
        s =[]
        for k in range(len(index)):
            s.append(df[cancer][index[k]])
        su.append(np.sum(s))
    sums.loc[:,'real'] = su
    
    # total counts
    tot = []
    for i in range(len(sets)):
        index = []
        for j in range(len(keys)):
            if len(set(sets[i])&keys[j]) >= 1:
                index.append(j)        
        t =[]
        for k in range(len(index)):
            t.append(df[cancer][index[k]])
        tot.append(np.sum(t))
    sums.loc[:,'total'] = tot
    
    
        # real fractions 
    realsum = 0
    for i in range(len(df[cancer])):
        if len(df.index[i]) >= cardinality:
            realsum += df[cancer][i]
    tops = np.array(sums.loc[:,'real'])
    fractions = 100*(tops/realsum)       
    sums.loc[:,'% of all real'] = fractions   
    
    #if len(callers) >= cardinality:   
        # real percentage difference, with respect to the initial two way intersection
    rpercent = []
    for i in range(len(sets)):
        rpercent.append(100*((sums['real'][i] - sums['real'][0]) / sums['real'][0]))
    sums.loc[:,'real % diff'] = rpercent
    
    # total percentage difference, with respect to the initial two way intersection
    tpercent = []
    for i in range(len(sets)):
        tpercent.append(100*((sums['total'][i] - sums['total'][0]) / sums['total'][0]))
    sums.loc[:,'total % diff'] = tpercent
    
    #sort by real percentage difference values
    if individual == False:
        sums = sums.sort_values(['real % diff'], ascending=False)
    
    if tab == True:
        #if len(callers) >= cardinality: 
        print(tabulate(sums, headers=['variant callers', 'real', 'real % diff', 'total', 'total % diff', '% of all real'], tablefmt='psql',floatfmt=(".0f",".0f",".3f", ".0f", ".3f",".3f")))
        #else:
        #    print(tabulate(sums, headers=['variant callers', 'real', 'total', '% of all real'], tablefmt='psql',floatfmt=(".0f",".0f",".0f", ".3f")))
        print()
    
    return sums