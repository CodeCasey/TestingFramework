##createReport.py
##This is used to create the report output of the results of our test cases for the Riot API Python Wrapper.
##after the test cases are executed, this report will be generated and opened into a browser window to display
##the results.
##Created By: Carson Smith, Brenard Casey, Daniel Feliciano 

import os

def reportCreate(testCases):

    headers = ['TestID: ', 'Requirement: ', 'Component: ', 'Method: ', 'Input: ', 'Expected Result: ', 'Test Result: ']
    currentDir = os.getcwd()
    reportURL = os.getcwd() + '/resultsReport.html'
    report = open(reportURL, 'w+')
    report.write('<html> <table border="1" style="width:85%"> \n')

    report.write("<tr> \n")
    for i in range(0, 7):
        report.write("<th>" + headers[i] + "</th> \n")
    report.write("</tr> \n")

    for i in range(1, 25):
        report.write('<tr> \n')
        report.write('<td>' + testCases[i].testID + '</td>')
        report.write('<td>' + testCases[i].testReq + '</td>')
        report.write('<td>' + testCases[i].testComp + '</td>')
        report.write('<td>' + testCases[i].testMethod + '</td>')
        report.write('<td>' + testCases[i].testInput + '</td>')
        report.write('<td>' + testCases[i].testOutcome + '</td>')
        if testCases[i].testResult == True:
            report.write('<td>' + 'Pass' + '</td>')
        else:
            report.write('<td>' + 'Fail' + '</td>')
        report.write('<tr> \n')

    report.write("</table> \n </html>")
    report.close
    return (reportURL)
