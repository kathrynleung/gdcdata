from inter import intersections
def set_contents(dat, possible_callers, keys):        
    data = dict([(key, []) for key in keys])
    
    patients = set(list(dat[0].keys()))
    for i in range(len(dat)):
        patients = patients & set(list(dat[i].keys()))
    
    
    for patient in patients:
        sets = []
        for j in range(len(dat)):
            sets.append(dat[j][patient])
        
        inters = intersections(sets)
        for i in range(len(inters)):
            data[keys[i]].extend(list(inters[i]))
       
    return data

