def union(*lists):
    if len(lists) == 0:
        print 'None'
        return []
    else:
        aset = set()
        for i in lists:
            aset = aset.union(set(i))
        return list(aset)

def union2(listoflst):
    if len(listoflst) == 0:
        print 'None'
        return []
    else :
        aset = set()
        for alist in listoflst:
            aset = aset.union(set(alist))
        return list(aset)

def intersect(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1.intersection(set2)

def difference(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1.difference(set2)

if __name__ == '__main__':
    s1 = [1,2,3]
    s2 = [2,3,4]
    s3 = [3,4,5]
    s11 = set(s1)
    s22 = set(s2)
    s33 = set(s3)
    print intersect(s1, s2)
