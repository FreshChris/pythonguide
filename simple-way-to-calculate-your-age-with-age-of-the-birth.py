import datetime 
brithYear = int(input("Enter your Brith Year:")) 
age = datetime.datetime.now().year - brithYear 
print("Your Age is", age, "Years Old")