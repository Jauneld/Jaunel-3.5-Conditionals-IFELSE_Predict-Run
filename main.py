#Jaunel Deans
#October 23, 2023
# We are predicting what the code will do when it runs. The predictions should be added to the code as comments.

# Example code 1

age = 18 #Assigning the value 18 to the defined variable age
 
if age > 18: # A if statment is created with the boolean to see if the age is greater than 18. 
 print("You are old enough to drive") #If the conditional is true, the print statement will print "You are old enough to drive". This will not output becasuse the conditional is false

# Example code 2

num1 = 1337 #Assigning the value 1337 to the defined variable num1
 
if num1 == 10: #A if statmentt is created with a conditional statement to see if the num1 is equal to 10.
  print("This text is output because the condition was true") #If the conditional is true, the indented code will run. The print statment will print "This text is output because the condition was true". 
else: # The else statement will print output the indented code if the if statment if false. 
  print("This text is output because the condition was false")  #If the conditional is false, the indented code will run. The print statment will print "This text is output because the condition was false". This will happen because num1's value is not equal to 10.

# Example code 3

number = 5#Assigning the value 5 to the defined variable number
print("I have thought of a number between 1 and 10")#Will print the statement "I have thought of a number between 1 and 10" to inspire a user to guess the number.
guess = int(input("Can you guess what it is?"))#Assigning the value of the interger input that the user typed in to the variable guess. The code will print out the statement "Can you guess what it is?" so the user can guess what the number is. If a decimal or a string is inputed there will be a Value Error because decimal values are floats and words are strings not whole numbers. 


if guess == number:#A if statment is created with a conditional statement to see if the value of guess is equal to the value of number
  print("Correct!") #if the conditional is true, the print statement will print "Correct!"
if guess < number: #A if statment is created with a conditional statement to see if the value of guess is less than the value of number 
  print("Too Low!")#if the conditional is true, the print statement will print "Too Low!"
if guess > number:#A if statement is created with a conditional statement to see if the value of guess is greater than the value of number
    print("Too High!")#if the conditional is true, the print statement will print "Too High!"

##My code allows the user to input a number larger the 10 and smaller the 1. An improvement to the code will require the user to stick to numbers between 0 to 10. 
  #if guess < 0 or guess > 10:
  #  print("Please enter a number between 0 and 10")
