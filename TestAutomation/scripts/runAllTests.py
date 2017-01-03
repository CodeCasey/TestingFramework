## runAllTests.py
## This is a test driver for the Riot Python Wrapper
## Created by: Daniel Feliciano, Carson Smith, Brenard Casey


import os
import webbrowser
from riotwatcher import RiotWatcher
from createReport import reportCreate

#This data is used to log in to the Riot Games API. It is independent of the Python wrapper or this test driver,
#it's just a requirement from Riot as a unique identifier for users 
#of their API.
region = 'NA1'
rWatcher = RiotWatcher('RGAPI-3088c62d-7884-4d77-9b32-5e614df09701')

testCases = []
currentDir = os.getcwd() #scripts folder
testCaseTextDir = currentDir + '/testCases'

#These objects are used to create a "Test Case", which is then pushed into an Array and cycled through when it
#is time to run the tests. These attributes follow our test case template as laid out in our report.
testID = None
testReq = None
testComp = None
testMethod = None
testInput = None
testOutcome = None
testResult = None

class TestCase:

    #A blank test case, this will be filled by reading the test case files and adding the information to this object. 
    def __init__(self, testID, testReq, testComp, testMethod, testInput, testOutcome, testResult):
        self.testID = testID
        self.testReq = testReq
        self.testComp = testComp
        self.testMethod = testMethod
        self.testInput = testInput
        self.testOutcome = testOutcome
        self.testResult = testResult

for subdir, dirs, files in os.walk(testCaseTextDir):
    for file in files:
        if '.txt' in file and 'SOURCES' not in file:
            openedfile = open(testCaseTextDir + '/' + file, 'r')
            for line in openedfile.readlines():
                if "1." in line:
                    temp = line.split("1.")
                    testID = temp[1]
                if "2." in line:
                    temp = line.split("2.")
                    testReq = temp[1]
                if "3." in line:
                    temp = line.split("3.")
                    testComp = temp[1]
                if "4." in line:
                    temp = line.split("4.")
                    testMethod = temp[1]
                if "5." in line:
                    temp = line.split("5.")
                    testInput = temp[1].strip()
                if "6." in line:
                    temp = line.split("6.")
                    testOutcome = temp[1].strip()
                    currentTest = TestCase(testID, testReq, testComp, testMethod, testInput, testOutcome, False)
                    testCases.append(currentTest)
        else:
            continue
        openedfile.close()

for i in range(1,27,1):
    if testCases[i].testMethod.strip() == 'static_get_champion':

        #####################Sample Information of Champions to compare to. These are the integers that will be returned by ##################################
        #####################static_get_champion and compared to the information supplied in the test cases for that method.##################################
        #Aatrox ID = 266
        #Anivia ID = 34
        #Alistar = 12
        #Amumu = 32
        #Blitzcrank = 53
        #Galio = 3
        results = rWatcher.static_get_champion(testCases[i].testInput)
        print("The expected oracle is : " + testCases[i].testOutcome)
        print("The actual oracle is : " + results['name'])
        testCases[i].testResult = testCases[i].testOutcome.strip() == results['name'].strip() #check to see if the name given in the testCase matches the result from the api
        print(testCases[i].testResult)
    if testCases[i].testMethod.strip() == 'static_get_item':
        results = rWatcher.static_get_item(int(testCases[i].testInput))
        #3001 - abyssal sceptre
        #3003 - archangels staff
        #3133 caulfields
        #3134 serrated dirk
        #3135 void staff
        print("The expected oracle is : " + testCases[i].testOutcome)
        print("The actual oracle is : " + results['name'])
        testCases[i].testResult = testCases[i].testOutcome.strip() == results['name'].strip()
        print(testCases[i].testResult)
    if testCases[i].testMethod.strip() == 'static_get_summoner_spell':
        results = rWatcher.static_get_summoner_spell(testCases[i].testInput)
        print("The expected oracle is : " + testCases[i].testOutcome)
        print("The actual oracle is : " + results['name'])
        testCases[i].testResult = testCases[i].testOutcome.strip() == results['name'].strip()
        print(testCases[i].testResult)
    if testCases[i].testMethod.strip() == 'static_get_mastery':
        results = rWatcher.static_get_mastery(testCases[i].testInput)
        print("The expected oracle is : " + testCases[i].testOutcome)
        print("The actual oracle is : " + results['name'])
        testCases[i].testResult = testCases[i].testOutcome.strip() == results['name'].strip()
        print(testCases[i].testResult)
    if testCases[i].testMethod.strip() == 'static_get_rune':
        results = rWatcher.static_get_rune(testCases[i].testInput)
        print("The expected oracle is : " + testCases[i].testOutcome)
        print("The actual oracle is : " + results['name'])
        testCases[i].testResult = testCases[i].testOutcome.strip() == results['name'].strip()
        #print(testCases[i].testResult)

report = reportCreate(testCases)
webbrowser.open_new_tab(report)
