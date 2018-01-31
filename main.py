inputSize = 784
middleSize = 32
outputSize = 10

sampleSize = 200
doSize = 50

#import data

import os
import csv
import random
import numpy as np

path = os.path.dirname( os.path.realpath(__file__) )
answer = 0

testingDataCSV = csv.reader( open(path + "/mnist_test.csv", "r") )
testingData = []

for row in testingDataCSV:
    testingData.append( [int(i) for i in row] )

d = testingData

#ai code


a = [
    np.zeros( inputSize ),
    np.zeros( outputSize )
]

w = [
    np.random.rand(inputSize, outputSize)
]

b = [
    np.zeros( inputSize ),
    np.zeros( outputSize )
]

def par0():
    pass

def par1():
    pass

def avg():
    pass

def prop():
    pass

def input():
    global answer
    answer = d[inpt][0]

    for i in range(0, inputSize):
        a[0][i] = d[inpt][i + 1] / 255

def output():
    m = -1
    r = -1

    for i in range(0, ouputSize):
        if a[1][i] > m:
            r = i
            m = a[1][i]

    return r































'''a = [ np.zeros( inputSize ) , np.zeros( middleSize ) , np.zeros( outputSize ) ]
w = [ np.random.rand(middleSize, inputSize) , np.random.rand(outputSize, middleSize) ]

def sigmoid(n):
    return 1 / (1 + np.exp(-n))

def dsigmoid(n):
    sig = sigmoid(n)
    return sig(1 - sig)

def foward():
    for i in range( middleSize ):
        sum = 0.0
        for j in range( inputSize ):
            sum += a[0][j] * w[0][j][i]
        self.a[1][i] = sigmoid(sum)

    for i in range( outputSize ):
        sum = 0.0
        for j in range( middleSize ):
            sum += self.a[1][j] * w[1][j][i]
        self.a[2] = sigmoid(sum)

def back():


def input():
    global answer
    answer = data[inpt][0]

    for i in range(0, inputSize):
        a[0][i] = data[inpt][i + 1] / 255

def output():
    m = -1
    r = -1

    for i in range(1, ouputSize):
        if a[2][i] > m:
            r = i
            m = a[2][i]

    return r

for i in range(0, doSize):
    correct = 0

    for i in range(0, samplesize):
        input( random.randint( 0, len(data) - 1 ) )
        foward()
        back()
        if output() == answer:
            correct++

    print( str(correct) + " / " + str(samplesize) + " correct" )'''