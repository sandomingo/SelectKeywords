#encoding=utf-8
import os
import sys
def doc2line(filename):
    docobj = open(filename)
    doc = docobj.read()
    try:
        doc = doc.decode('gb18030')
        doc_str = ''.join(doc.split())
        return doc_str
    except Exception, e:
        print e
        return ''
    finally:
        docobj.close()

def dirall2one(paths, outname):
    out = open('./out/'+outname, 'w')
    try:
        for path in paths:
            filelist = os.listdir(path)
            for afile in filelist:
                astr = doc2line(path+'/'+afile)
                if astr == '':
                    continue
                out.write(astr.encode('utf-8'))
                out.write('\n')
    except Exception, e:
        print e
    finally:
        out.close()

def print_useage():
    print "Usage: python fileutil.py outname path [path2 path3 ...]"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_useage()
    else:
        paths = sys.argv[2:]
        outname = sys.argv[1]
        dirall2one(paths, outname)
