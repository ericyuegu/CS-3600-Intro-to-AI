from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)


## TESTING

"""
q5penData = []
q5carData = []

for n in range(5):
	nnet, testAccuracy = testPenData()
	q5penData.append(testAccuracy)

	nnet2, testAccuracy2 = testCarData()
	q5carData.append(testAccuracy2)

print "~~~ Q5 ~~~"
print "PEN DATA ACCURACY", q5penData
print "max: ", max(q5penData)
print "average: ", average(q5penData)
print "stDev: ", stDeviation(q5penData)
print "\nCAR DATA ACCURACY", q5carData
print "max: ", max(q5carData)
print "average: ", average(q5carData)
print "stDev: ", stDeviation(q5carData)
"""

# dict<int/list>
penoutput = {}
caroutput = {}
perceptrons = 0
while perceptrons <= 40:
	q6penData = []
	q6carData = []

	for n in range(5):
		nnet, testAccuracy = testPenData(hiddenLayers = [perceptrons])
		q6penData.append(testAccuracy)

		nnet2, testAccuracy2 = testCarData(hiddenLayers = [perceptrons])
		q6carData.append(testAccuracy2)

	penStats = {}
	penStats['max'] = max(q6penData)
	penStats['average'] = average(q6penData)
	penStats['stDev'] = stDeviation(q6penData)
	penoutput[perceptrons] = (q6penData, penStats)

	carStats = {}
	carStats['max'] = max(q6carData)
	carStats['average'] = average(q6carData)
	carStats['stDev'] = stDeviation(q6carData)
	caroutput[perceptrons] = (q6carData, carStats)

	perceptrons += 5

print "~~~ Q6 ~~~"
print "\nPEN DATA"
for p in penoutput:
	print "Perceptrons: ", p
	print penoutput[p]
print "\nCAR DATA"
for p in caroutput:
	print "Perceptrons: ", p
	print caroutput[p]