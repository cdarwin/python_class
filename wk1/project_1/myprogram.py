#!/usr/bin/python -O

import sys

infile = open(sys.argv[1],'r')
outfile = open(sys.argv[2],'w')

for line in infile:
  num = line.split()
  s = ""

  if len(num) < 3:
    outfile.write("Malformed line\n")

  if num[0] == "+":
    res = 0
    for i in range(len(num)-2):
      res += int(num[i+1])
      s += "{0} + ".format(num[i+1])
    res += int(num[-1])
    s += "{0} = {1}\n".format(num[-1], res)
    outfile.write(s)
  elif num[0] == "-":
    res = int(num[1])
    for i in range(len(num)-2):
      res -= int(num[i+2])
      s += "{0} - ".format(num[i+1])
    s += "{0} = {1}\n".format(num[-1], res)
    outfile.write(s)
  elif num[0] == "*":
    if len(num) > 3:
      outfile.write("Malformed line\n")
    else:
      res = int(num[1])*int(num[2])
      s = "{0} * {1} = {2}\n".format(num[1], num[2], res)
      outfile.write(s)
  elif num[0] == "/":
    if len(num) > 3:
      outfile.write("Malformed line\n")
    else:
      res = float(num[1])*float(num[2])
      s = "{0} / {1} = {2}\n".format(num[1], num[2], res)
      outfile.write(s)
  else:
    outfile.write("Malformed line\n")

infile.close()
outfile.close()
