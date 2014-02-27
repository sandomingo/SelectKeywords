#encoding=utf-8
from __future__ import division
import os
import sys
import textutil
import util
import time

'''给一个文件,每行包括一个文档，输出该集合中在绝大多数文档出现的词语表'''
def run(path, topN=50, encoding='utf-8'):
    word_stats = {} # word : num of docs which contains the word
    afile = open(path)
    docnum = 0
    for line in afile:
        fcontent = None
        try:
            fcontent = line.decode(encoding)
        except Exception, e:
            print 'Decode Error occur in:', path
        if fcontent == None or fcontent == '':
            continue
        docnum += 1
        fsegs = textutil.seg_doc(fcontent)
        words = set() # words that occur in the doc
        for seg in fsegs:
            seg = seg.strip()
            if len(seg) > 1:
                words.add(seg)
        for word in words:
            if word in word_stats:
                # increase doc number
                word_stats[word] += 1
            else:
                word_stats[word] = 1
    afile.close()
    #remove stop word
    textutil.dictkey_remove_stopwords(word_stats)
    #find max number of exact word in docs
    wmax = 0
    for k,v in word_stats.items():
        if wmax < v:
            wmax = v;
    #calculate tfidf
    idfdic = textutil.getidfdic()
    for k,v in word_stats.items():
        if k in idfdic:
            word_stats[k] = v / wmax * idfdic[k]
        else:
            word_stats[k] = 0
    wordnum = len(word_stats)
    print 'Doc num: ', docnum, 'total words num:', wordnum, ' topN:', topN
    # sort by word occurance DESC, now word_stats is a list
    word_stats = util.sort_dic_byvalue(word_stats, rev=True)
    frontier = int(topN)
    counter = 0
    result = []
    for (k,v) in word_stats.items():
        if counter < frontier:
            # print k.encode('utf-8'), v
            result.append(k)
            counter += 1
        else:
            break
    return result, word_stats

def get_content(path, filename, encoding='utf-8'):
    filepath = path + '/' + filename
    fstr = open(filepath).read().decode(encoding)
    return fstr

def print_useage():
    print 'Usage: python modewords.py file_path[, topN]'

if __name__ == '__main__':
    testpath = '/Users/SanDomingo/wspace/WorkspacePython/topkeyword/test/test.txt'
    argsnum = len(sys.argv)-1
    if argsnum == 3:
        path = sys.argv[1]
        if path == 'test':
            path = testpath
        topN = int(sys.argv[2])
        encoding = sys.argv[3]
        run(path, topN, encoding)
    elif argsnum == 2:
        path = sys.argv[1]
        if path == 'test':
            path = testpath
        topN = int(sys.argv[2])
        run(path, topN)
    elif argsnum == 1:
        path = sys.argv[1]
        if path == 'test':
            path = testpath
        start_ts = time.time()
        run(path)
        elipse = time.time() - start_ts
        print 'Time consume: ', elipse,'second'
    else:
        print_useage()
