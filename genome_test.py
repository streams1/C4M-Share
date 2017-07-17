import re
f = open("/share/data/day5/puzzle.txt")
lines = f.readlines()
list = []
seq = ""
for w in lines:
    w = w.replace(",","")
    m = w.strip()
    parts = m.split()
    list = list + parts    
seq = seq + list[0]    
print seq
i = 0
x = seq[-4:]
print x
while i < len(list):
  x = seq[-4:]
  y = seq[0:4]
  fate = raw_input("search first 4 or last 4 of seq: ") 
  if fate == 'last 4':
    for e in list:
      s = re.search(x,e)
      if s:
         print e
      else:
         print "", 
  elif fate == 'first 4':
    for e in list:
      s = re.search(y,e)
      if s:
         print e
      else:
         print "",
  ask = raw_input("What do you want me to add: ")
  where = raw_input("Where do you want me to add this (front or end): ")
  if where == 'front':
     seq = ask + seq
  else:
     seq += ask
  print seq
  for e in list:
    s = re.search(e,seq)
    if s:
       del list[i]
    else:
       continue 
  print list
