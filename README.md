功能说明：
    该项目用来对构成全集的N个类别做关键词提取。提取的步骤如下：
        1. 使用jieba分词，去除停用词，长度为1的字
        2. 对每个类别的文档进行计算，统计包含某个候选词的文档个数，以此记为该候选词的词频（TF）
        3. 计算每个候选词TF-IDF值，取topN进入下一步算法
    计算每个类别的关键词如下：
        1. 每个类别的关键词各自构成一个集合，计算每个类别中不在其他任意集合中的关键词最为最终代表该类别的关键词。
        2. 这一步产生的结果依然按TF-IDF值排序，可以取topN

使用方法：
    该项目主要使用两个py文件。
    1. modeinN.py 生成关键词
    Usage: python modein3.py dirpath, TOPN
    dirpath为包含多个类别的文档文件，每个类别对应一个文件，文件的每一行对应一篇文本
    输出到stdout，可以使用重定向到任意输出文件(e.g: out.txt)
    2. genkwfile.py 解析modeinN.py输出，产生每个类对应的关键词文件
    Usage: python genkwfile.py rawfile topN
    使用在rawfile同路径下输出N个文件，分别为各自类别选择的关键词
