__author__ = 'admin'
import sys
import re
import os
import os.path
import platform
import json

def runJmx(srcFile, destFile):
    # implement MxTerminator (java version)
    os.system('java -cp jmx/mxpost.jar eos.TestEOS jmx/eos.project < ' + srcFile + ' > ' + destFile)


def getWordFreqDict(originalstr):
    L = re.split('\W+',originalstr)     # non-character
    freqDict = {}
    for e in L:
        # deal with digits
        if e.isdigit():
            e = '<digit>'
        # convert into lowercase
        e = e.lower()
        if e not in freqDict:
            freqDict[e]=0
        freqDict[e] += 1

    del freqDict['']
    # '' should be deleted, because
    # if str is like 'apple,banana.' re.split('\W+',str) will return 'apple' 'bananna' ''
    # also, if str is like '.apple' re.split('\W+',str) will return '' 'apple'
    return freqDict

if __name__ == '__main__':
    destFile = sys.argv[1]
    if(os.path.isdir(sys.argv[2])):
        srcFileNames = os.listdir(sys.argv[2])
        srcFiles = map(lambda f:sys.argv[2]+'/'+f, srcFileNames)
    else:
        srcFiles = [sys.argv[2]]

    print 'dest:',destFile

    # Use MxTerminator for sentence splitting
    if(len(sys.argv) == 4 and sys.argv[3] == '-jmx'):
        print 'run jmx'
        for (srcFile,srcFileName) in zip(srcFiles, srcFileNames):
            if (os.path.isdir(srcFile) or srcFile.endswith('sen')):
                continue
            runJmx(srcFile, sys.argv[2]+'/'+'sen'+'/'+srcFileName)
        # Redirect srcFiles
        srcFiles = os.listdir(sys.argv[2]+'/'+'sen')
        srcFiles = map(lambda f:sys.argv[2]+'/sen/'+f, srcFiles)


    fout = open(destFile,'w')
    for srcFile in srcFiles:
        if os.path.isdir(srcFile):
            continue
        print 'parsing src:'+srcFile
        fin = open (srcFile,'r')

        sen_cnt = 0
        output_dict ={}
        for sentence in fin:
            output_dict['s_'+str(sen_cnt)] = getWordFreqDict(sentence)
            sen_cnt += 1
        fin.close()

        fout.write(os.path.basename(srcFile)+' '+json.dumps(output_dict)+'\n')
    fout.close()
