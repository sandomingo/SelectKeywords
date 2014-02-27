from collections import OrderedDict
def printids(filename='rzx-0220/category-tech.txt', target = 'CATEGORY$tech|'):
    obj = open(filename)
    for i, line in enumerate(obj):
            line = line.decode('utf-8')
            if line.find(target) >= 0:
                print i+1

def sort_dic_bykey(adic, rev=False):
    return OrderedDict(sorted(adic.iteritems(), key=lambda d:d[0], reverse=rev))

def sort_dic_byvalue(adic, rev=False):
    return OrderedDict(sorted(adic.iteritems(), key=lambda d:d[1], reverse=rev))


