from sklearn.tree import DecisionTreeClassifier as DTree
import csv
import numpy as np
import random
import pickle
#Numbebr of rows randomly selected from data
MAX = 200000

#Function to get random rows from cleaned data
def splitData(inputEle, output):
	a = []
	b = []
	file = "analyzed.csv"
	with open(file, 'r') as csvFile:
		csvWr = csv.reader(csvFile, delimiter=',')
		for row in csvWr:
			rowNumeric = []
			for i in range(len(row)-1):
				rowNumeric.append(float(row[i]))
			a.append(rowNumeric)
			b.append(row[-1])
	print "Finished reading data"
	rangeList = range(len(a))
	random.shuffle(rangeList)
	index = 0
	for i in rangeList:
		if index > MAX:
			break
		index += 1
		inputEle.append(a[i])
		output.append(b[i])
	del a[:]
	del b[:]
	print "Data shuffling done"

#Function to train model and save it in pickle file
def model(inputEle, output):
	splitData(inputEle,output)
	splitIndex = int(.50*len(inputEle))
	print splitIndex
	trainData = inputEle[:splitIndex]
	testData = inputEle[splitIndex:]
	trainOutput = output[:splitIndex]
	testOutput = output[splitIndex:]
	print "Data splitting done"
	npOutput = np.array(trainOutput)
	npInput = np.array(trainData)
	clf = DTree().fit(npInput, npOutput)
	pickle.dump(clf, open('test.pkl', 'w'))
	print "Pickle created"


def main():
	inputEle =  []
	output = []
	model(inputEle, output)
	count = 0
	#Beginning Testing
	'''clf2 = pickle.load(open('test.pkl'))
	for i in range(len(inputEle)):
		z = clf2.predict(inputEle[i])
		print  z[0], output[i]
			count += 1
	print count
	result = "\ncorrect is: "+ str(count)+" and total is: "+str(len(inputEle))
	with open("out.txt", 'a') as file:
		file.write(result)
'''
if __name__ == '__main__':
	main()