# # num1 = 5.5
# # print(type(num1))

# #  lear about complex numbers
# # complex numbers are specified as <real part>+<imaginary part>j

# # compNum=  5+7J
# # print(compNum)


# # str1="""name
# # mohasmm
# # msos"""
# # print(str1)

# #  data type  IN PYTHON
# # 1.  int
# # 2.  float
# # 3.  complex
# # 4.  String

# # 5.  Boolean
# # what is boolean
# # 0 = false
# # 1 = true
# # bool1 = True
# # print(bool1)

# # 6.  List
# # what is list
# # list is a collection of items in a particular order
# # nameOfList = [item1, item2, item3, item4]
# # can access item by index and can accept any type of data

# # lis1 = ['asdsad', 2.6, 3+6j, [4,'jdsjds'], 5, 6, 7, 8, 9]
# # index[0,         1,   2,     3,          4, 5, 6, 7, 8]
# # index : represent the position of item in list
# # index start from 0
# # print(lis1[3][1])
# # lis1[3][1] = 'changed'
# # print(lis1[3][1])
# # 7.  Tuple

# # what is tuple
# # tuple is a collection of items in a particular order
# # nameOfTuple = (item1, item2, item3, item4)
# # can access item by index and can accept any type of data
# # tuple is immutable

# # tupl1= ('asdsad', 2.6, 3+6j, [4,'jdsjds'], 5, 6, 7, 8, 9)
# # print(tupl1[3][1])
# # tupl1[0] = 'changed'
# # print(tupl1[0])

# # 8. dectionary
# # what is dictionary
# # dictionary is a collection of key value pairs
# # nameOfDictionary = {key1:value1, key2:value2, key3:value3}
# # person = {'name': 'mohammad', 'age': 28, 'address': 'irbid'}

# # print(person['age'])

# # quiz : create a dictionary that contains your name, age, address, phone number, and email
# # also print your name and email
# # then change your age and print it again



# # name= input('enter your name: ')
# # x = len(name)
# # finalString = ''
# # # for i in range(x) :
# # #     if name[i] == 'l':
# # #         finalString = '*'


# # print(name)
# # print(finalString)




# # name= 'sallem'

# # name= name[0:2]+'*'+ name[3:]
# # print(name)

# # name = input('enter your name: ')
# # # create for loop to replace all 'l' with '*'

# # for i in range(len(name)):
# #     if name[i] == 'l':
# #         name = name[0:i] + '*' + name[i+1:]
# # print(name)

# # # use replace function to replace all 'l' with '*'

# # for i in range(len(name)):
# #     if name[i] == 'l':
# #         name = name.replace('l', '*')
# # print(name)


# #  if statement
# #  elif statement
# #  else

# # num1 = int(input('enter first number: '))

# # if num1 > 0:
# #     print('positive')
# # elif num1 < 0:
# #     print('negative')
# # else:
# #     print('wrong input ')

# # what is loop in python

# # while num1 > 0:
# #     print(num1)
# #     num1 -= 1

# # odd or even number

# # oddOrOven = int(input('enter number: '))
# # if oddOrOven % 2 == 0:
# #     print('even')
# # else:
# #     print('odd')


# # prime or not
# # primeOrNot = int(input('enter number: '))


# # for i in range(2, primeOrNot):
# #     if primeOrNot % i == 0:
# #         print('not prime')
# #         break

# # else:
# #     print('prime')

# #  take 3  input from the user As astring and check if this string have l or u or both and
# # replace it with * and print the new string

# #  3 checks fro prime or odd or even for each
# #  and all the task must be inside while loop

# #Q1
# # x=0
# # while x<3:
# #     checkString=input ('enter a string: ')
# #     for i in range(len(checkString)):
# #          if ((checkString[i]=='l') or checkString[i]=='u'):
# #               checkString= checkString[0:i]+'*'+checkString[i+1:]
# #         # replace method in python
# #                 checkString=checkString.replace('l','*')

# #     print(checkString)


# #     num=int(input('enter the number: '))
# #     if (num%2)==0:
# #         print('the number ia even')
# #     else :
# #         print('the number is odd')

# #     prime=int(input('enter the number : '))
# #     for i in range (2,prime):
# #         if (prime%i)==0:
# #             print ('not prime')
# #             break
# #     else :
# #         print('prime')
# #     x = x+1

# # function in python
# # what is function
# # function is a block of code that can be called by its name and can be used again and again

# # we also send data to function as parameters

# # def functionName(parameter1, parameter2, parameter3):
# #    # code
# #   # return value

# # call function
# # functionName(argument1, argument2, argument3)

# # def printName(name):
# #     # print('hello ' + name)
# #     return ('hello ' + name)

# # print(printName('mohammad'))


# # num1= int(input('enter first number: '))
# # num2 = int(input('enter second number: '))

# # def sumAndMultiply(first,second):
# #     sumation = first + second
# #     multy = first * second
# #     return ('sumation is: ' + str(sumation) + ' and multy is: ' + str(multy))

# # print(sumAndMultiply(num1,num2))

# #  I have a hamster.
# #    My hamster's name is Harry.
# # answer = 'yes'
# # while answer != 'no':
# #     animalType = input('enter animal type: ')
# #     animalName = input('enter animal name: ')

# #     def printAnimal(type, name):
# #         return ('I have a ' + type + '.\nMy ' + type + "'s name is " + name + '.')
# #     print(printAnimal(animalType, animalName))

# #     print('do you want to continue?')
# #     answer = input('enter yes or no: ')


# #     while answer != 'yes' and answer != 'no':
# #         print('wrong input')
# #         answer = input('enter yes or no: ')

# # print('thank you')

# ## create 2 funiction iside while loop
# ## 3 input from the user as father name and mother name username
# ##  print greating for the user
# # print if the user mother or father name is longer or shorter than the username


# # list1 = ['mohammad', 'ahmad', 'sallem', 'mohammad', 'ahmad', 'sallem']
# # print(list1[2:5])

# # function : block of code that we can creat it and declare it and call it
# # method : block of code that we can use it without creat it or declare it
# # range : range(start, end, step)
# # variable : container for data
# # counter = 0
# # for i in list1:
# #     print(i == 'mohammad')
# #     if i == 'mohammad':
# #         list1[counter] = 'changed'
# #     counter += 1
# # print(list1)

# # list1= list1 + ['changed']
# # print(list1)

# # append : add item to the end of the list
# # list1.append('changed')

# # print(list1)

# # list1 = list1[0:2] + ['changed'] + list1[2:]
# # print(list1)


# # list1.insert(2 , 'changed')
# # print(list1)
# # list2 = [1,2,3,4,5]
# # # list1= list1 + list2
# # # print(list1)

# # # extend : add list to the end of the list
# # list1.extend(list2)
# # # print(list1)
# # list3 = [ -1,2,3,4,5,6,7,8,9,100,10,2,6,3]
# # sumation = 0
# # for i in list3:
# #     sumation += i
# # print(sumation)
# # print(sum(list3))

# # # for i in list3:
# # #     if i == 10:
# # #         sumation += 1
# # # print(sumation)

# # # count : count the number of times the item is repeated in the list

# # print(list3.count(10))

# # # len : return the length of the list

# # len(list3)

# # # index : return the index of the item in the list

# # print(list3.index(10))
# # maxValue = list3[0]
# # minValue = list3[0]

# # for i in list3:
# #     if i > maxValue:
# #         maxValue = i

# #     if i < minValue:
# #         minValue = i

# # print(maxValue)
# # print(minValue)
# # list3 =  list3[-1:]
# # print(list3)
# # counters = -1
# # list4 =[]
# # for i in range(len(list3)):
# #     print(i)
# #     list4.append(list3[counters])
# #     counters -= 1
# # print(list4)
# # list3.reverse()
# # print(list3)
# # sort : sort the list

# # list3.sort(reverse=True)
# # print(list3)

# # pop : remove item from the list using index
# # list3.pop(7)
# # print(list3)

# # remove : remove item from the list using value

# # list3.remove(100)
# # print(list3)

# # create a list of 10 numbers and print the sum of these numbers but the list should
# # have 2 numbers as string and the rest as numbers also int and float
# # avarage of the list
# # max and min of the list
# # print the index of the max and min of the list
# #

# # list2 = [1,2,3,4,5,'a',7,'8',9,10]
# # sumation = 0
# # for i in list2:
# #     try :

# #         sumation += int(i)
# #     except ValueError:
# #         print('wrong value')


# # print( sumation)

# # dectionary : collection of key value pairs



# #  -----------------------

# # ------------

# # person = {
# #     'name' : 'mohammad',
# #     'age' : 28,
# #     'city' : 'irbid',
# # }

# # person['job'] = 'developer'
# # person['skills']= ['java', 'python']
# # person['parents']= {
# #     'father':'ahmad',
# #     'mom':'lina',
# #     'son':{
# #         'name':'ali',
# #         'age':16

# #     }
# # }
# # print(person)


# # for loob : print the key and the value of the dec

# # for i in person:
# # print(i + ' : ' + str(person[i]))


# # methods in dectonary :

# # clear :

# # person.clear()
# # print(person)

# # copy : copy one list to anouther

# # decNew = {}
# # decNew=person.copy()
# # print(decNew)

# # items : get all items in the dec
# # print(person.items())

# # keys : print all keys in the dec

# # print(person.keys())

# # Valus : to print all valus in the list
# # print(person.values())

# # pop : remove for item inside the dec

# # person.pop('job')
# # print(person)
# # print(person['parents']['son']['name'])

# # print(person['skills'][0:3])

# # popitem
# # print(person)
# # person.popitem()
# # print(person)

# # update

# # person.update({"city": "amman"})
# # person['city']= 'amman'
# # print(person)


# # home work

# # create claSSROOM DEC
# # user input
# # 1 ask the useer to enter the name of the student
# # ask the user to enter the age of the student
# # cuity, job ,parents(dec),age,skils(list)
# # at nthe end ask the user if he want to add new student or not
# # print all the students in the class
# #       mohammad
# # age:  28

# # # home work of dec
# # def getStudentInformation():
# #     studentName= input('Enter the student name: ')
# #     studentAge =int(input('Enter the student age :'))
# #     studentCity=input('Enter the city  where the student live : ')
# #     studentJob=input ('Enter the job of the student : ')
# #     print ('Enter the parent information')
# #     fatherName =input('Enter name of the student father : ')
# #     motherName =input('Enter name of the student mother : ')
# #     parents={'mother':motherName,'father':fatherName}
# #     skillsElements = int(input("Enter the number of skills you have : "))
# #     skills = []
# #     for i in range(skillsElements):
# #         user_input = input("Enter the skill: ")
# #         skills.append(user_input)
# #     return{
# #         'name':studentName,
# #         'age':studentAge,
# #         'city':studentCity,
# #         'job':studentJob,
# #         'Parents':parents,
# #         'skills':skills
# #     }
# # classRoom={}
# # newStudent='yes'
# # whileCondition = True
# # while whileCondition:
# #     if newStudent=='yes':
# #         print ('\n Enter the student information ')
# #         studentInformation = getStudentInformation()
# #         classRoom[studentInformation['name']] =studentInformation
# #         newStudent= input("Do you want to add more students? (yes/no): ")
# #     elif newStudent=='no' :
# #         whileCondition = False
# #         print("\nClassroom Dictionary:")
# #         for student_name, student_info in classRoom.items():
# #                         print(f"Name: {student_info['name']}")
# #                         print(f"Age: {student_info['age']}")
# #                         print(f"City: {student_info['city']}")
# #                         print(f"Job: {student_info['job']}")
# #                         print("Parents:")
# #                         print(f"\tmother : {student_info['Parents']['mother']}")
# #                         print(f"\tfather: {student_info['Parents']['father']}")
# #                         print("Skills:", ", ".join(student_info['skills']))
# #                         print('-----------------------------------')


# #  classes : is a blue print for creating objects

# # class Student:

# class Student:


#     def __init__(self, name ='sam', age=20, job='student',location='irbid'):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.location = location

#     def printName(self):
#         print("my name is "+self.name)

#     def __str__(self):
#         return f'name : {self.name} , age : {str(self.age)} , job : {self.job}, location : {self.location}'


# #  send job name age to the class in unordered way
# obj3 = Student()
# obj1 = Student('dev', 28, 'mohammad')
# obj2 = {'name':'ali', 'age':16, 'job':'student'}
# print(obj3)

# # # class Clinet:
# # #     name = 'mohammed'
# # #     age = 27
# # #     city = 'riyadh'

# # # client1= Clinet()
# # # print(client1.name)

# # # #  class has attributes and methods
# # # # what is the difference between attributes and methods
# # # # attributes are variables
# # # # methods are functions



# # #  cars
# # #  models> color> power >company> year> price> type>
# # print('*'*70)
# # print('welcome to our car show room')
# # print('my app is about cars')
# # print('you can add a car by entering the model, color, power, company, year, price and type')
# # print('*'*70)
# # cars=[]
# # while True:
# #     car={}
# #     car['model'] = input('enter the model:')
# #     car['color'] = input('enter the color:')
# #     car['power'] = input('enter the power:')
# #     car['company'] = input('enter the company:')
# #     car['year'] = int(input('enter the year:'))
# #     car['price'] = int(input('enter the price:'))
# #     car['type'] = input('enter the type:')
# #     cars.append(car)
# #     if input('do you want to add an other car?') == 'no':
# #         break
# # for i in range(len(cars)):
# #     print('*'*70)
# #     print('car number', i+1)
# #     for j in cars[i]:
# #         print(j, ':', cars[i][j])


# # #  pationts
# # #  name> medican> doctor>insurance >hospital>age


# # # computers
# # #  storage> ram> cpu> company> price> type> color> year

# # #  trasportation mode
# # #  mode > travil time> fule consumption> amustions> cost> repare cost

# class BankAcount:



#     def __init__(self, name ='', num= 0, balance = 0,password=''):
#         self.acc_name = name
#         self.acc_num = num
#         self.acc_balance = balance
#         self.password = password

#     def __str__(self):
#         return f'name is {self.acc_name} and number is {self.acc_num} and balance is {self.acc_balance}'

#     def withdraw(self,amount ):
#         passw= input('enter your password:')
#         if passw == self.password:

#             try:
#                 if self.acc_balance < int(amount):
#                     print('you do not have enough money')
#                     return 'you do not have enough money'
#                 self.acc_balance -= int(amount)
#                 print(f'your balance is {self.acc_balance} and you withdraw {amount}')
#                 return f'your balance is {self.acc_balance} and you withdraw {amount}'
#             except ValueError:
#                 print('you should enter a number')
#                 return 'you should enter a number'
#         else:
#             print('wrong password')
#             return 'wrong password'

#     def deposit(self,amount):
#         try:

#             self.acc_balance += int(amount)
#             print(f'your balance is {self.acc_balance} and you Deposit {amount}')
#             return f'your balance is {self.acc_balance} and you Deposit {amount}'
#         except ValueError:
#             print('you should enter a number')
#             return 'you should enter a number'
#     def checkBalance(self):
#         print(f'your balance is {self.acc_balance}')
#         return f'your balance is {self.acc_balance}'
#     def closeAccount(self):
#         print('you are about to close your account')
#         passw= input('enter your password:')
#         if passw == self.password:
#             self.acc_name = 'closed account'
#             self.acc_num = 0
#             self.withdraw(self.acc_balance)
#             self.acc_balance = 0
#             print('your account is closed')
#             return 'your account is closed'
#         else:
#             print('wrong password')
#             return 'wrong password'


# account2= BankAcount('ahmad', 123456, 1000,'2333')
# print(account2)
# account2.withdraw('200')
# # # account2.deposit('500')
# # account2.checkBalance()
# account2.closeAccount()
# print(account2)
#  random method to generate a random number
import random

# print(testNum1)

class BankAccount:
    acc_name=''
    acc_num=0
    balance=0
    def generateAccountNumber(self):
        accountNumber =[]
        for i in range(6):
            testNum =random.randint(1,9)
            accountNumber.append(testNum)
        x =0
        for i in range(len(accountNumber)):
            x = x*10 + accountNumber[i]
        return x
    def __init__(self,acc_name,balance,password):
        self.acc_name=acc_name
        self.acc_num=self.generateAccountNumber()
        self.balance=balance
        self.password=password
    def __str__(self):
        return f'name is {self.acc_name} and the account number is {self.acc_num} and the belence is {self.balance}'
    def withdraw(self, amount):
       print ('you are about to withdraw.')
       passw=input('enter your password to confirme you withdraw operation : ')

       try:
            if(self.password==passw):
              if (self.balance)<int(amount):
                  return 'you do not have engough money'
              self.balance-=int(amount)
              return (f'your balance is {self.balance} and you withdraw {amount}')
            else :
                return('you enter wrong password')
       except ValueError:
              return 'you entered wrong value '
    def deposit (self, amount):
        print('you are about to deposite.')
        passw=input('enter your password to confirme your deposite operation : ')
        try:
           if(self.password==passw):
              self.balance+=int(amount)
              return (f'your balance is {self.balance} and you deposit {amount}')
           else :
                return('you enter wrong password')
        except ValueError:
            return 'you entered wrong value '
    def checkAccount(self):
        return f'your balance {self.balance}'
    def closeAccount (self):
        print('you are about to close your account.')
        passw=input('enter your password to confirme your closeing operation : ')
        print(self.withdraw(self.balance))
        self.acc_name='The account is closed'
        self.acc_num=0
        self.balance=0
        return f'your account is closed '
    def transfer(self):
        print('you are about to transfer')
        try:
            while True:
                passw=input('enter your password to confirm our transfer operation')

                if (self.password==passw):
                    receiver=input('enter the account number of the receiver')
                    print (len(accounts))
                    for i in range(len(accounts)):
                        if accounts[i].acc_num==int(receiver):
                            print('1- transfer all your money')
                            print('2- transfer a certain ammount')
                            choice=input('enter your choice')
                            if choice=='1':
                              pass
                            elif choice =='2':
            
                                print('enter the amount you want to transfer')
                                amount=input
                                self.balance-=amount
                                accounts[i].balance+=int(amount)
                                print('you transfered {amount} to {receiver.acc_name} so your current balance is {self.balance}')
                                
                        else:
                            return('you entered a wrong password')
        except ValueError:
            return'you entered a wrong value'


accounts=[]
while True:

    print('*'*50)
    print('welcome to our bank')
    print('do you have an account with us?')
    print('1- yes')
    print('2- no')
    choice=input('enter your choice: ')
    if choice=='2':
        userName=input('enter your name :')
        accbalance=int(input('enter the balance in your account :'))
        passwor=input('enter you password: ')

        account1=BankAccount(userName,accbalance,passwor)
        for i in range(len(accounts)):
            if account1.acc_num==accounts[i].acc_num:
                        account1=BankAccount(userName,accbalance,passwor)
        accounts.append(account1)
        print(account1)

    elif choice=='1':
        username = input('enter your account number :')
        password = input('enter your password :')
        for i in range(len(accounts)):
            if accounts[i].acc_num==int(username) and accounts[i].password==password:
                print('1- Transfer money')
                print('2- close account')
                print('3- withdraw')
                print('4- deposit')
                print('5- check balance')
                print('6- exit')
            
                choice=input('enter your choice: ')
                print(choice)
                if choice=='1':
                    accounts[i].transfer()
                elif choice=='2':
                    print(accounts[i].closeAccount())
                elif choice=='3':
                    amount=input('enter the amount you want to withdraw: ')
                    print(accounts[i].withdraw(amount))
                elif choice=='4':
                    amount=input('enter the amount you want to deposit: ')
                    print (accounts[i].deposit(amount))
                elif choice=='5':
                    print(accounts[i].checkAccount())
                elif choice=='6':
                    break
                else:
                    print('you entered wrong choice')
    
