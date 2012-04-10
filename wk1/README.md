# Python – Week 1 Projects

These two projects constitute the lab work for week 1 of the Taos Python class. They are designed to be  quite doable during the 2-hour lab time, as long as you have viewed the lectures beforehand.

All completed work should be submitted via Moodle. Do not email, print, or send via carrier pigeon.

## Project 1: Infix Batch Calculator

You will write a batch calculator that takes input as a text file, one set of calculations per line. All items on a single line are space separated.

To run: 

    ./myprogram.py infile outfile

**Input file specification:**

Operator operand1 operand2…

+ 2 2

* 2 3

etc…

**Output file specification:**

Write the results in standard infix notation:

Operand1 + operannd2 = result….

2 + 2 =4

2 * 3 = 6

* Stage 1:
  * Support addition, subtraction, multiplication, and division of two operands
* Stage 2:
  * Add support for more than two operands for addition and subtraction
  * Add intelligent errors about supporting more than two operands for multiplication and division
* Stage 3:
  * Look at the documentation for the Python “math” library
  * Add functions from the math library, give intelligent errors on anything that does not use the correct number of operands
* Stage 4:
  * Add support for handling parenthesis on the same line
  * Input format is something like: + (* 2 3) (* 4 5)
  * Output here would be (2 * 3) + (4 * 5) = 26

## Project 2: Simple Grep

You will write a simple replacement for the Unix “grep” utility

Grep reads a file (or standard input, if there is no file) and returns lines that meet a specific search criteria. It can read one or more files.

Usage: 

    ./mygrep.py spam myfile.txt

* Stage 1:
  * Simple string searches
  * Single file or standard in, depending on command line arguments
* Stage 2:
  * Add regular expression search
  * Add –v command line option (show lines not containing search)
* Stage 3:
  * Add –i (ignore case) command line option
  * Add –F (simple string match, fgrep equivalent) command line option
* Stage 4:
  * Add additional command line arguments / functionality from grep
  * You choose what to add!
