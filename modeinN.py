#encoding=utf-8
import modewords
import setop
import sys
import os
import time
import util

def run(dir_path, TOPN):
    filelst = os.listdir(dir_path)
    filenamelst = []
    wlst_lst = []
    word_stats = []
    for afile in filelst:
        # skip non txt file
        print 'file processing', afile
        if afile.lower().find('txt') == -1:
            continue
        awlst, awstats= modewords.run(dir_path + '/' + afile, TOPN)
        filenamelst.append(afile)
        wlst_lst.append(awlst)
        word_stats.append(awstats)
        print 'file processed', afile

    wlsts = setop.union2(wlst_lst)

    wdic = {} # doc_type : keywords

    for index, item in enumerate(wlst_lst):
        # union all list except wlst_lst[index]
        otherlsts = []
        for index2, item in enumerate(wlst_lst):
            if index != index2:
                otherlsts.append(wlst_lst[index2])
        owlsts = setop.union2(otherlsts)
        wi = setop.difference(wlsts, owlsts)
        # sort the keyword by tfidf
        wordscoredict = {}
        for item in wi:
            wsdict = word_stats[index]
            wordscoredict[item] = wsdict[item]
        wordscoredict = util.sort_dic_byvalue(wordscoredict, rev=True)
        wdic[filenamelst[index]] = wordscoredict
    printutf8dict(wdic)

def printutf8dict(adic):
    for k,v in adic.items():
        print 'Docs:', k.encode('utf-8')
        for item,value in v.items():
            print item.encode('utf-8'), value
        print ''

def print_useage():
    print 'Usage: python modein3.py dirpath, TOPN'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        dirpath = sys.argv[1]
        TOPN = sys.argv[2]
        start_ts = time.time()
        run(dirpath, TOPN)
        elipse = time.time() - start_ts
        print 'Time consume: ', elipse,'second'
    else:
        print_useage()
