inputs = 784
middles = 32
outputs = 10

samples = 100
doSize = 20

rate = .25

#import data

import os
import csv
import random
import numpy as np

path = os.path.dirname( os.path.realpath(__file__) )

testingDataCSV = csv.reader( open(path + "/mnist_test.csv", "r") )
testingData = []

for row in testingDataCSV:
    testingData.append( [int(i) for i in row] )

data = testingData

#ai vars

a = [
    np.zeros( inputs ),
    np.zeros( outputs )
]

w = [
    np.random.rand(inputs, outputs)
]

#ai func

def actFunc(x):
    return x

#ai interface

def foward():
    for t in range(outputs):
        a[1][t] = 0
        for n in range(inputs):
            a[1][t] += a[0][n] * w[0][n][t]
        a[1][t] = actFunc(a[1][t])

def back():
    for t in range(outputs):
        for n in range(inputs):
            if a[0][n] > 0:
                if (t == answer):
                    c = a[0][n]
                else:
                    c = -a[0][n]
                w[0][n][t] = min( max( w[0][n][t] + c * rate , 0 ) , 1 )

#io

answer = 0

def input(inpt):
    global answer
    answer = data[inpt][0]

    for i in range(inputs):
        a[0][i] = data[inpt][i + 1] / 255

def output():
    m = -1
    r = -1

    for i in range(outputs):
        if a[1][i] > m:
            r = i
            m = a[1][i]

    return r

#main loop

for n in range(doSize):
    correct = 0

    for i in range(samples):
        input( random.randint( 0, len(data) - 1 ) )
        foward()
        back()
        if output() == answer:
            correct += 1

        #print(a)

    print( str(n + 1) + ": " + str(correct) + " / " + str(samples) + " correct" )



'''

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

'''





























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