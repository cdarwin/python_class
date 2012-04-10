#!/usr/bin/python -O

import sys

infile = open(sys.argv[1],'r')
outfile = open(sys.argv[2],'w')

for line in infile:
  i = line.split()

  if i[0] == "+":
    j = int(i[1])+int(i[2])
  elif i[0] == "-":
    j = int(i[1])-int(i[2])
  elif i[0] == "*":
    j = int(i[1])*int(i[2])
  elif i[0] == "/":
    j = float(i[1])*float(i[2])
  else:
    break

  s = "{0} {1} {2} = {3}\n".format(i[1], i[0], i[2], j)
  outfile.write(s)

infile.close()
outfile.close()
