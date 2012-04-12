#!/usr/bin/python -O

import sys

def addition(num): # return string containing result of addition
  """Calculate the addition of the numbers provided and return a string of the result"""
  res = 0
  for i in xrange(1,len(num)):
    res += int(num[i])
  s = ' + '.join(num[1:]) + ' = ' + str(res) + '\n'
  return s

def subtraction(num): # return string containing result of subtraction
  """Calculate the subtraction of the numbers provided and return a string of the result"""
  res = int(num[1])
  for i in xrange(2,len(num)):
    res -= int(num[i])
  s = ' - '.join(num[1:]) + ' = ' + str(res) + '\n'
  return s

def multiplication(num): # return string containing result of multiplication
  """"Calculate the multiplication of the numbers provided and return a string of the result"""
  if len(num) > 3:
    s = 'Malformed line\n'
  else:
    res = int(num[1])*int(num[2])
    s = '{0} * {1} = {2}\n'.format(num[1], num[2], res)
  return s

def division(num): # return string containing result of division
  """"Calculate the division of the numbers provided and return a string of the result"""
  if len(num) > 3:
    s = 'Malformed line\n'
  elif num[2] == 0:
    return ('DIVIDE BY ZERO ERROR')
  else:
    res = float(num[1])*float(num[2])
    s = '{0} / {1} = {2}\n'.format(num[1], num[2], res)
  return s

def main():
  infile = open(sys.argv[1],'r')
  outfile = open(sys.argv[2],'w')

  for line in infile:
    num = line.split()
  
    if len(num) < 3:
      outfile.write('Malformed line\n')
  
    if num[0] == '+':
      outfile.write(addition(num))
    elif num[0] == '-':
      outfile.write(subtraction(num))
    elif num[0] == '*':
      outfile.write(multiplication(num))
    elif num[0] == '/':
      outfile.write(division(num))
    else:
      outfile.write('Malformed line\n')
  
  infile.close()
  outfile.close()

if __name__ == "__main__":
  main()
