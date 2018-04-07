# GMIT-Data Analytics
Repository for Course Exercises and Projects only. 
For general testing, learning, major blunders and other scripts please see repository https://github.com/andreroche/Test-Scripts

# exercise2.py
Combination of exercises 1&2. This is a program that displays Fibonacci numbers using people's names. Text was changed from original author to surname 'Roche' and is commented in the program. The output of the program is:

My surname is Roche
The first letter R is number 82
The last letter e is number 101
Fibonacci number 183 is 78569350599398894027251472817058687522


The ord() returns the ASCII value/code of a character as per the ASCII-Binary conversion chart since computers only understand bits/bytes etc.

In this program and referencing the chart in the video tutorial, upper case R is 082 and lower case e is 101. 

# Exercise3.py
This is a program to test the Collatz Conjecture using While, If and Else statements. See Collatz Conjecture on the web @ https://en.wikipedia.org/wiki/Collatz_conjecture
The program is commented to include all references used in creating the program.

# Exercise4.py
Euler Problem 5  - see www.projecteuler.net
All references used to create this code are commented within the program. The program actually takes too long to compute if you start at 2 (because all numbers are divisible by 1) and increment or counter to 20. Numbers in the range 11-20 are used (although this could also be shortened) because 1-10 is already computed in the question. The start point used is 2520 and increments of 2520 are used (since 1-10 evenly divide into this, this number must evenly divide into the number i'm looking for)  

Answer from program is The LCM of numbers 1-20 is 232792560

# Exercise5.py
Input/Output using Fisher's Iris Data Set - see https://en.wikipedia.org/wiki/Iris_flower_data_set for more information.
All references and documentation used for learning are commented within the program.
Before running this program please ensure that the data set is saved to 'working directory/data/iris.csv'
The first part of the program reads in the variable data from the data set (which is downloaded to the working directory) and outputs data in an easily readable table within the terminal window. Please extend the window to display correctly.
The second part of the program uses additional learning. It uses the CSV reader and writer modules and is useful for working with CSV files. It also makes it easier to read in all data but filter it accordingly so only the necessary information is displayed. It gives the user the added benefit of having formatted data in an external file (as opposed to the terminal window) which could be then imported into other application software for analysis etc. 

# Exercise6.py
A Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. The factorial of a number is that number multiplied by all of the positive numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 120. The script tests the function by calling it with the values 5, 7, and 10. It only accepts positive integers i.e. not letters, words, negative numbers or numbers with decimal points.
