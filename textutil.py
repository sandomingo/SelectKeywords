import jieba
def read2list(filename, type,encoding='utf-8'):
    obj = open(filename)
    if type == 'lst':
        lst = []
        for line in obj:
            item = line.decode(encoding)
            lst.append(item.strip())
        return lst
    elif type == 'dic':
        dic = {}
        for line in obj:
            key,value = line.decode(encoding).split()
            dic[key.strip()] = float(value.strip())
        return dic

def getidfdic():
    idfdic = read2list('idf.txt', 'dic', 'utf-8')
    return idfdic

def dictkey_remove_stopwords(adict):
    stopwordlst = read2list('stopwords.txt', 'lst', 'gb18030')
    for k in adict.keys():
        if k in stopwordlst:
            adict.pop(k)

def seg_doc(doc_str):
    seg_list = jieba.cut(doc_str)
    return seg_list
