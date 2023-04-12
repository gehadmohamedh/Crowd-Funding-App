import re
def readNum(s):
    while True:
        num = input(s)
        if num.isnumeric():
            return int(num)
        print("please enter number !!")

def readString (s):
    while True:
        num = input(s)
        if num.isalpha():
            return str(num)
        print("please enter alphapet characters  !!")

def validateEmail():
    while True:
        s = input("Enter Your Email ")
        regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        if(re.search(regex,s)):
          print("Valid Email")
          return s 
        else:
          print("Invalid Email")

def validateDate(s):
    while True:
        date = input (s)
        date_pattern = re.compile(r'^(?!0000)[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')

        if date_pattern.match(date):
            print("Valid date ")
            return date 


        else:
            print("Invalid date")