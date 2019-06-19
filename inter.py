from comb import my_combs
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