import pickle

#STN and YEARMODA is required
def predictOutput(stn, wban, yearmoda, temp, dewp, slp, visib, wdsp, mxspd, gust, prcp):
	#Assigning default values
	if wban is None:
		wban = 99999
	if temp is None:
		temp = 9999.9
	if dewp is None:
		dewp = 9999.9
	if slp is None:
		slp = 9999.9
	if visib is None:
		visib = 999.9
	if mxspd is None:
		mxspd = 999.9
	if gust is None:
		gust = 999.9
	if prcp is None:
		prcp = 99.9
	inputEle = [stn, wban, yearmoda, temp, dewp, slp, visib, wdsp, mxspd, gust, prcp]
	inputFin = [float(x) for x in inputEle]
	#Predict
	clf2 = pickle.load(open('test.pkl'))
	z = clf2.predict(inputFin)
	result = str(int(float(z[0])))
	outputList = []
	#Make 6 digits
	length = len(result)
	result = ('0'*(6-length)) + result
	#Convert to string
	if result[0] == '1':
		outputList.append('Fog')
	if result[1] == '1':
		outputList.append('Rain')
	if result[2] == '1':
		outputList.append('Snow')
	if result[3] == '1':
		outputList.append('Hail')
	if result[4] == '1':
		outputList.append('Thunder')
	if result[5] == '1':
		outputList.append('Tornado')
	#Return result
	return  outputList

#This is how you need to call this function
def main():
	result = predictOutput(8403,99999,20140309,87.9,61.2,1009.4,6.2,2.1,8.9,14,99.9)#Give your input here
	for item in result:
		print item

if __name__ == '__main__':
    main()