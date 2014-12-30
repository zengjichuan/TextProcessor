__author__ = 'admin'
import sys
import re
import os
import os.path
import platform

def runJmx(srcFile, destFile):
    # implement MxTerminator (java version) in Windows
    oss = platform.system()
    if oss=='Windows':
        os.system('java -cp jmx/mxpost.jar eos.TestEOS jmx/eos.project < ' + srcFile + ' > ' + destFile)
    elif oss=='Linux':
        print 'linux'
    elif oss=='Darwin':
        print 'Mac'

def getWordFreqDict(originalstr):
    L = re.split('\W+',originalstr)
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

    # fout = open(destFile,'a')
    for srcFile in srcFiles:
        if os.path.isdir(srcFile):
            continue
        print 'parsing src:'+srcFile
        fin = open (srcFile,'r')

        sen_cnt = 0


