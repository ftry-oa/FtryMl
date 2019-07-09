import numpy
import os
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = numpy.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances  = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def img2vector(filename):
    file = open(filename)
    mat = numpy.zeros((1, 1024))
    for i in range(32):
        line = file.readline()
        for j in range(32):
            mat[0, 32*i+j] = int(line[j])
    file.close()
    return mat

def getLabelByFilename(filename):
    if len(filename) == 0:
        return ''
    prefix = filename.split('.')[0]
    label = prefix.split('_')[0]
    return label

def handleWriting(txtPath):
    # 1 获取训练样本
    trainingLables = []
    pwd = os.getcwd()
    trainingDirname = '/FtryMl/pages/kNN/trainingDigits'
    trainingFileList = os.listdir(pwd + trainingDirname)
    m = len(trainingFileList)
    trainingMats = numpy.zeros((m, 1024))
    i = 0
    for trainingFilename in trainingFileList:
        label = getLabelByFilename(trainingFilename)
        trainingLables.append(label)
        trainingMats[i, :] = img2vector(pwd + trainingDirname + '/' + trainingFilename)
        i = i + 1
    # 2 测试
    testMat = img2vector(txtPath)
    testLabel = classify0(testMat, trainingMats, trainingLables, 3)
    return testLabel
