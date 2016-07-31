import numpy as np
import  jieba
import  copy
import codecs,sys

ftest1fn = "D:\Tempory\mobile2.txt"
ftest2fn = "D:\Tempory\war2.txt"

sampfn = "D:\Tempory\war1.txt"

def get_cossimi(x,y):
    myx = np.array(x)
    myy = np.array(y)
    cos1 = np.sum(myx * myy)
    cos21 = np.sqrt(sum(myx * myx))
    cos22 = np.sqrt(sum(myy * myy))
    return cos1 / (cos21 * cos22)

if __name__ == '__main__':
    print("loading...")
    print("working...")

    f1 = codecs.open(sampfn,"r","utf-8")
    try:
        f1_text = f1.read()
    finally:
        f1.close()

    f1_seg_list = jieba.cut(f1_text)
    #first test
    ftest1 = codecs.open(ftest1fn,"r", "utf-8")
    try:
        ftest1_text = ftest1.read()
    finally:
        ftest1.close()
    ftest1_seg_list = jieba.cut(ftest1_text)

    #second test
    ftest2 = codecs.open(ftest2fn, "r", "utf-8")
    try:
        ftest2_text = ftest2.read()
    finally:
        ftest2.close()
    ftest2_seg_list = jieba.cut(ftest2_text)

    #read sample text
    #remove stop word and constructor dict
    f_stop = codecs.open("D:\Tempory\stopwords.txt","r","utf-8")
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split("\n")

    test_words = {}
    all_words = {}

    for myword in f1_seg_list:
        print(".")
        if not(myword.strip()) in f_stop_seg_list:
            test_words.setdefault(myword, 0)
            all_words.setdefault(myword, 0)
            all_words[myword] += 1

    #read to be tested word
    mytest1_words = copy.deepcopy(test_words)
    for myword in ftest1_seg_list:
        print(".")
        if not(myword.strip()) in f_stop_seg_list:
            if myword in mytest1_words:
                mytest1_words[myword] += 1

    mytest2_words = copy.deepcopy(test_words)
    for myword in ftest2_seg_list:
        print(".")
        if not(myword.strip()) in f_stop_seg_list:
            if myword in mytest2_words:
                mytest2_words[myword] += 1

    #calculate sample with to be tested text sample
    sampdate = []
    test1data = []
    test2data = []
    for key in all_words.keys():
        sampdate.append(all_words[key])
        test1data.append(mytest1_words[key])
        test2data.append(mytest2_words[key])
test1simi = get_cossimi(sampdate,test1data)
test2simi = get_cossimi(sampdate,test2data)

print("{0}样本{1}的余弦相似度{2}".format(ftest1fn,sampdate,test1simi))
print("{0}样本{1}的余弦相似度{2}".format(ftest2fn,sampdate,test2simi))





