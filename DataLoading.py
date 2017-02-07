import numpy as np
import os, glob
import csv

#Function to rename all the files
def renameData(path):
	for dirpath, dirnames, filenames in os.walk(path):
		for fileName in dirnames:
			filePath, ext = os.path.split(os.path.abspath(fileName))
			fileName = filePath+"\\Extracted\\" + fileName + "\\" + fileName
			#print(fileName)
			newName = fileName[:-3] + ".txt"
			os.rename(fileName, newName)

#Function to check if a string is float
def checkFloat(num):
	try:
		float(num)
		return True
	except:
		return False


#Function to read data from all the files
def readData(path, output):
	start = True

	#Put column names manually
	cols = ["STN---", "WBAN", "YEARMODA", "TEMP", "TEMP_COUNT", "DEWP", "DEWP_COUNT", "SLP", "SLP_COUNT", "STP", "STP_COUNT", "VISIB", "VISIB_COUNT", "WDSP", "WDSP_COUNT", "MXSPD", "GUST", "MAX", "MIN", "PRCP", "SNDP", "FRSHTT"]
	for dirpath, dirnames, filenames in os.walk(path):
		for fileName in dirnames:
			filePath, ext = os.path.split(os.path.abspath(fileName))
			#This path is hard coded and will be changed according to system
			#Reason being there seems to be some issue with os.path.abspath
			#It gives path of the project while it should give path of file
			currfileName = filePath + "\\Extracted\\" + fileName + "\\" + fileName[:-3] + ".txt"
			print(currfileName)
			lineNum = 0

			#Selecting how to open CSV file
			if start:
				option = 'w+'
				start = False
			else:
				option = 'a+'

			with open(currfileName) as file, open("analyzed.csv", option) as csvFile:
				csvWr = csv.writer(csvFile, delimiter=',')
				for line in file:
					lineNum += 1
					if lineNum <= 1 or len(line) < 1:
						continue

					#Break line into columns
					line = line.split()

					#Clean the columns
					line[17] = line[17][:-1]
					line[18] = line[18][:-1]
					line[19] = line[19][:-1]

					#Remove COUNT columns
					line.pop(14)
					line.pop(12)
					line.pop(10)
					line.pop(8)
					line.pop(6)
					line.pop(4)
					#Remove columns which are not strongly correlated with FRSHTT
					line.pop(14)
					line.pop(12)
					line.pop(11)
					line.pop(6)
					#For making it suitable for models
					line2 = [float(x) for x in line]
					#Enter the row into csv file
					csvWr.writerow(line2)


#Function to write data to a CSV file
def writeOutput():
	fileName = "data2.csv"
	with open(fileName, 'r') as csvFile:
		csvWr = csv.reader(csvFile, delimiter=',')
		for row in csvWr:
			print(','.join(row))


def main():
	path = "Extracted/"#Folder inside project where unzipped files are stored
	#renameData(path)
	output = []
	readData(path, output)
	#writeOutput()


if __name__ == '__main__':
    main()