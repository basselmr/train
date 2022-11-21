# for comments in Python
#------------------------
#name = input ("your name ??")
#print ("Hello " , name)
#a = input ("input a :")
#b = input ("input b :")
#c = int(a) + int(b)
#print ("a = ",a ,"b = ",b)
#print (a ," + ", b , "=" ,c)
#----------------------------
#print (int(98.6))
#----------------------------
#hrs = input("Enter Hours")
#rate = input("Enter Rate:")
#pay = float(hrs) * float(rate)
#print ("Pay:",pay)
#-------------------------------

#     if elif  else
#-------------------
#x=5
#print ("the value of x is : "+str(x))
#if x >=5:
#    print("x is greater or equal 5")
#elif x < 20:
#    print("x is smaller than 20")
#else:
#    print("x is greater than 20")
#print ("Finish")
#--------------------

#       try  except         
#---------------------------
#astr = 'Hello Bob'
#try:
#    istr = int(astr)
#except:
#    istr = -1
#print ('First',istr)
#--------------------------

#--------------------------
# if statement exanple
#hrs = input("Enter Hours : ")
#h= float(hrs)
#rate = input("Enter Hour Rate : ")
#r=float(rate)
#if h<=40:
#    pay=h*r
#else:
#    pay=(40*r)+((h-40)*(r*1.5))
#print(pay)
#--------------------------

#       using functions in Python
#--------------------------------------
#def thing():
#    print("Hello")
#    print("Fun")
#thing()
#print ("Zip")
#thing()
#---------------------------------------
#     Function Example ............#
#---------------------------------------
#def getScore(x):
#    score = input("Please Enter :")
#    try:
#        score=float(score)
#        score = score * x
#        return score
#    except:
#        print("Please Enter number :")
#        getScore()
#print(getScore(5))
#--------------------------------------
#          Loops in Python         #
#--------------------------------------
#x=5
#while x>0:
#    print(x)
#    x=x-1
#print("Loop Ended")
#--------------------------------------

#-------------------------------------
#while True:
#    line=input(">")
#    if line=="done":
#        break
#    if line[0]=='#':
#        continue
#    print(line)
#print("Done!")
#--------------------------------------

#-------------------------------------
#for x in range (1,6):
#    print("x="+str(x))
#print("")
#for y in range (1,6,2):
#    print("y="+str(y))
#print("")
#friends=['josph','glenn','sally']
#for fr in friends:
#    print("Happy new year "+str(fr))
#--------------------------------------

#--------------------------------------
#numbers=[41,12,9,3,74,15]
#max=0
#min=None
#total=0
#average=0
#count=0
#for n in numbers:
#    count=count+1
#    total= total+n
#    if n>max:
#        max=n
#    if min is None:
#        min=n
#    elif n<min:
#        min=n
#average=total/count
#print("max number : "+str(max))
#print("min number : "+str(min))
#print("sum numbers : "+str(total))
#print("Average number : "+str(average))
#--------------------------------------

#--------------------------------------
#num=0
#tot=0.0
#while True :
#    sval=input('Enter a number : ')
#    if sval=='done':
#        break
#    try:
#        fval=float(sval)
#    except:
#        print('Invalid  input')
#        continue
#    num=num+1
#    tot = tot + fval
#print('All Done')
#print (tot,num, tot/num)
#--------------------------------------

#--------------------------------------
#            JSON Object in PUTHON     
#--------------------------------------
#import json
##some JSON:
#x =  '{ "name":"John", "age":30, "city":"New York"}'
## parse x:
#y = json.loads(x)
## the result is a Python dictionary:
#print(y["age"])


