#Louna Akkad 1-5-2018
#this program calculate BMR BMI TDEE
import re
import sys

#validaing the name
while True:
  check_name = re.compile('([a-zA-Z])+')
  print ('Name should contain At least one character')
  name = input('Enter your name: ')
  if check_name.match(name):
    break
  else:
    print ('Name should contain At least one character')
print ('************************************************************88')
	
#validating the gender

while True:
  print ('Gender should be M or F (upper or lower case')
  gender = input('Enter your Gender: ')
  if gender=='F' or gender=='f' or gender=='m' or gender=='M':
    break
  else:
    print ('Gender should be M or F (upper or lower case')
print ('************************************************************88')

#validaing the weight

while True:
  print ('weight should be At least 100 pounds')
  weight =  int(input('Enter your weight: '))
  if (weight>=100):
    break
  else:
    print ('weight should be At least 100 pounds')
print ('************************************************************88')
	
#validaing the height

while True:
  print ('height should be Between 60 to 84 inches, inclusive')
  height =  int(input('Enter your height: '))
  if (height>=60 and height<=84 ):
    break
  else:
    print ('height should be Between 60 to 84 inches, inclusive')
print ('************************************************************88')
	
#validaing the age

while True:
  print ('age should be At least 18 years old')
  age =  int(input('Enter your age: '))
  if (age>=18):
    break
  else:
    print ('age should be At least 18 years old')
print ('************************************************************88')
	
#validaing 	Activity Level
	
while True:
  print ('Activity Level should be Between 1 to 5, inclusive')
  Activity_Level = int(input('Enter your Activity_Level: '))
  if ( Activity_Level>=1 and Activity_Level<=5 ):
     break
  else:
    print ('Activity Level should be Between 1 to 5, inclusive')
print ('************************************************************88')
		
########################################################################
#convert units
weight_kg=weight*0.45359237 
height_cm=height/0.39370
#calulate bmr for both genders
if gender=='F' or gender=='f':
    BMR = 66 + (13.7 * weight_kg) + (5 * height_cm) - (6.8 * age) 
else:
    BMR = 655 + (9.6 * weight_kg) + (1.8 * height_cm) - (4.7 * age)
#calulate bmi
BMI = ((weight* 703) / (height*height)) 
#get Description
if BMI< 18.5:
  msg='Your are Underweight'
elif BMI >= 18.5 and BMI<25:
  msg='Your are Normal weight'
elif BMI >=25 and BMI < 30:
  msg='Your are Overweight'
else :
   msg='Your are Obese'
 ########################################################33
 
#calulate Total Daily Energy Expenditure
if Activity_Level == 1:
    TDEE=BMR * 1.2
if Activity_Level==2:
     TDEE=BMR * 1.375
if Activity_Level==3 :
     TDEE=BMR * 1.55
if Activity_Level==4:
     TDEE=BMR * 1.725
if Activity_Level==5:
     TDEE=BMR * 1.9
print ('************************************************************')
print ('Your Name is:',name)
print ('Your Gender is:',gender)
print ('Your height inch is:',height)
print ('Your weight pounds is:',weight)
print ('Your Activity_Level is:',Activity_Level)
print ('************************************************************')
print ('Your BMR is',round(BMR))
print ('Your BMI is',round(BMI))
print (msg)
print ('Your Total Daily Energy Expenditure is',round(TDEE))
















	
	
	
	
	
	
	
	
	
	

