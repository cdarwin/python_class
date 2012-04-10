## Project 1: Infix Batch Calculator

You will write a batch calculator that takes input as a text file, one set of calculations per line. All items on a single line are space separated.

To run: 

    ./myprogram.py infile outfile

**Input file specification:**

Operator operand1 operand2…

"+ 2 2"

"* 2 3"

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
