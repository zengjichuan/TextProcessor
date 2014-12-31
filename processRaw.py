import getopt

__author__ = 'admin'
# This is a script running on raw text materials. The output
# Step one: remove stop word
# Step two: compute word frequency
# How to use?

import re
import os
import os.path
import sys

def getWordFreq(originalstr):
    L = re.split('\W+',originalstr)


def main(argv):
    inputfile = ''
    outputfile = ''
    stopwordfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'processRaw.py -stopword <stopwordFile> -output <outputFile> -input <inputFile> -tf | -idf'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-stopword':
            stopwordfile = arg
            sys.exit()
        elif opt == '-output':
            outputfile = arg
        elif opt == '-input':
            inputfile = arg
    destFile = sys.argv[1]

    if(os.path.isdir(inputfile)):
        srcFileNames = os.listdir(sys.argv[2])
        srcFiles = map(lambda f:sys.argv[2]+'/'+f, srcFileNames)
    else:
        srcFileNames = [sys.argv[2]]
        srcFiles = [sys.argv[2]]

    # create output dir if doesn't exist
    if not os.path.exists(os.path.dirname(destFile)):
        os.makedirs(os.path.dirname(destFile))
    print 'dest:',destFile

    # remove stop word
    if
    fout = open(destFile,'a')
    for srcFile in srcFiles:
        if os.path.isdir(srcFile):
            continue
        print 'parsing src:'+srcFile
        fin = open(srcFile,'r')
        sen_cnt = 0
        output_dict = {}
        for sentence in fin:
            output_dict['s_'+ str(sen_cnt)] = getWordFreq(sentence)
            sen_cnt += 1
        fin.close()
        fout.write(os.path.basename(srcFile))

    fout.close()


    if __name__ == '__main__':
        main(sys.argv[1:])