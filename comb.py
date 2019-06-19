from itertools import combinations

def parse_maf(fp):
    ''' Return a dictionary with vars[patient][variant_set]'''
    caller_vars = {}

    fh = open(fp, 'r')
    for line in fh:
        temp = line.strip().split('\t')
        if line[0] == '#' or temp[0] == 'Hugo_Symbol':
            continue
        ID = temp[16] + '_' + temp[17] # 'tumor'_'normal'
        if ID not in caller_vars:
            caller_vars[ID] = set()
        gene = temp[0]
        chrom =temp[4]
        s_pos = temp[5]
        e_pos = temp[6]
        ref = temp[11]
        tum_allele_1 = temp[12]
        tum_allele_2 = temp[13]
        impact = temp[93]
        filt = temp[110]
        var = (gene,chrom, s_pos, e_pos, ref, tum_allele_1, tum_allele_2,impact, filt)
        caller_vars[ID].add(var)

    return(caller_vars)

def my_combs_frozenset(iterable, r):
    to_return = []
    for i in range(1, r+1):
        c = combinations(iterable, i)
        for comb in c:
            to_return.append(frozenset(comb))
    return to_return

def my_combs_all(iterable, r):
    to_return = []
    for i in range(1, r+1):
        c = combinations(iterable, i)
        for comb in c:
            to_return.append(list(comb))
    return to_return

def my_combs(iterable, r):
    c = combinations(iterable, r)
    to_return = []
    for comb in c:
        to_return.append(comb)
    return to_return

def my_combos(iterable, r):
    c = combinations(iterable, r)
    to_return = []
    for comb in c:
        to_return.append(list(comb))
    return to_return
"""
def intersections(list_of_sets):
    '''
    Given a list of sets, returns all possible exclusive intersections of the sets.
    '''
    sets = list_of_sets
    combs = []
    inters = []
    ret = []

    for i in range(len(sets)):
        combs.append(my_combs(range(len(sets)), abs(len(sets)-i)))
        inter = []
        for comb in combs[i]:
            intersect = sets[comb[0]]
            for j in range(len(comb)):
                intersect = intersect & sets[comb[j]]
            for j in range(i):
                for comb2, inter2 in zip(combs[j], inters[j]):
                    condition = True
                    for k in range(len(comb)):
                        condition = condition and (comb[k] in comb2)
                    if condition is True:
                        intersect -= inter2
            inter.append(intersect)
        inters.append(inter)
    
    for j in range(len(sets)):
        ret.extend(inters[len(sets)-1-j])
    
    return ret
    """