# Python3 code to calculate age in years 
from datetime import date 

def calculateAge(birthDate): 
	days_in_year = 365.2425	
	age = int((date.today() - birthDate).days / days_in_year) 
	return age 
		
# Driver code 
 
print("Please enter your date of birth:") 
a=int(input("Your year 4 digits:"))
b=int(input("Your month 2 digits:"))
c=int(input("Your day 2 digits:"))
print(calculateAge(date(a, b, c)), "years")