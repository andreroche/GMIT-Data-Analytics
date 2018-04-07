def factorial(f): # define factorial 'f'.
    if f == 0: # equality operator. If f is 0
        return 1 # return the value 1.
    else: # else statement.
        return f * factorial(f-1) # return the factorial of the integer 'f'

while True: # start of while loop - while the condition is a '1'. 
    f = input('Input a number to compute the factorial: ') # request to user on screen to input a number. 
    if f.isdigit(): # is f a positive integer? .
        break    # exit the loop. 

f=int(input("Repeat selection to compute the factorial : ")) # repeat the prompt for integer selection on screen. 


print(factorial(f)) # print to screen factorial for 'f' i.e. the input positive integer.


print("The expected factorial for 5 should be 120, The result is : ", factorial(5)) # proof that the factorial computaiton is working.
print("The expected factorial for 7 should be 5040, The result is : ", factorial(7)) # proof that the factorial computaiton is working.
print("The expected factorial for 10 should be 3628800, The results is : ", factorial(10)) # proof that the factorial computaiton is working.


# I am aware that this program can be improved upon. It has a flaw where if the user inputs a positive integer (error checking) and
# then is prompted to repeat the selection but selects a non positive integer the program crashes. 