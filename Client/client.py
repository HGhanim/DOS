import requests
import sys

FRONTEND_IP = 'http://192.168.1.176:5000'

while(True):
    print("\n*****Welcome to Bazar.com book store!*****\n")
    print("Choose one of the following operations:")
    print("Search [1]")
    print("Info [2]")
    print("Purchase [3]")
    print("Exit [4]")
    original_stdout = sys.stdout
    try:
        operationNum = int(input('Operation Number: '))
    except ValueError:
        print("Enter a valid number")
        continue
    if(operationNum == 1):
        bookSubject = str(input('Book Subject: '))
        requestURL = FRONTEND_IP + '/search/' + bookSubject
    elif(operationNum == 2):
        bookId = str(input('Book Id: '))
        requestURL = FRONTEND_IP + '/info/' + bookId
    elif(operationNum == 3):
        bookId = str(input('Book Id: '))
        requestURL = FRONTEND_IP + '/purchase/' + bookId
    elif(operationNum == 4):
        break
    else:
        print("Enter a valid number")
        continue
        
    with open('output.txt', 'a') as f:
        sys.stdout = f
        print("Request:")
        print(requestURL + "\n")
        try:
            if(operationNum == 1 or operationNum == 2):
                response = requests.get(requestURL)
            elif(operationNum == 3):
                response = requests.put(requestURL)
            print("Response: ")
            print(response.json())
            print("Response Status:")
            print(response.status_code)
        except:
            print("No response, an error has occured.")
        
        print("\n***********************\n")
        sys.stdout = original_stdout


