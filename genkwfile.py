#encoding=utf-
import sys

LINE_PREFIX = 'Docs: '
def run(rawfile, topN):
    fobj = open(rawfile)
    topN = int(topN)
    docs = []
    titles = []
    docid = -1
    for line in fobj:
        line = line.decode('utf-8').strip()
        if len(line) == 0:
            continue
        elif line.find(LINE_PREFIX) == 0:
            title = line
            titles.append(title)
            docs.append([])
            docid += 1
        else:
            word = line.split()
            if len(word) == 2:
                docs[docid].append(word[0])

    # write list to file
    docnum = len(titles)
    for i in range(docnum):
        outfilename = titles[i].split()[1].split('.')[0] + '.keyword'
        out = open(outfilename, 'w')
        icounter = 0
        for line in docs[i]:
            out.write(line.encode('utf-8') + '\n')
            icounter += 1
            if icounter >= topN:
                break
        out.close()
        print 'output: outfilename, total', icounter,'key words.'

def print_usage():
    print 'Usage: python genkwfile.py rawfile topN'

if __name__ == '__main__':
    argvnum = len(sys.argv)
    if argvnum == 3:
        rawfile = sys.argv[1]
        topN = sys.argv[2]
        run(rawfile, topN)
    else:
        print_usage()


