def how_many_tumor(cancer, coadread, content, dictofgenes, filt, impacts, keys):
    if cancer == 'COAD' or cancer == 'READ':
        tumorcount = []
        for key in keys:
            count = 0
            for c in content[key]:
                if set(c) & coadread:
                    if set(c) & impacts:
                        if set(c) & filt:
                            count += 1
            tumorcount.append(count)
    else:
        tumorcount = []
        for key in keys:
            count = 0
            for c in content[key]:
                if set(c) & dictofgenes[cancer]:
                    if set(c) & impacts:
                        if set(c) & filt:
                            count += 1
            tumorcount.append(count)
    return tumorcount

def how_many_tumor_cgc(content, cgc, filt, impacts, keys):
    tumorcount = []
    for key in keys:
        count = 0
        for c in content[key]:
            if set(c) & set(cgc['Gene Symbol']):
                if set(c) & impacts:
                    if set(c) & filt:
                        count += 1
        tumorcount.append(count)
    return tumorcount

def how_many(content,filt, impacts, keys):
    counts = []
    for key in keys:
        count = 0
        for c in content[key]:
            if set(c) & impacts:
                if set(c) & filt:
                    count += 1
        counts.append(count)
    return counts


def how_many_pancan(content, pancandict, filt, impacts, keys):
    tumorcount = []
    for key in keys:
        count = 0
        for c in content[key]:
            if set(c) & pancandict:
                if set(c) & impacts:
                    if set(c) & filt:
                        count += 1
        tumorcount.append(count)
    return tumorcount

def how_many_impact(content, keys, level):
    impact = []
    for key in keys:
        count = 0
        for c in content[key]:
            if c[7] == level:
                count += 1
        impact.append(count)
            
    return impact