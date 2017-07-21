f = open("/share/data/day5/puzzle.txt")
lines = f.readlines()
list = []
for w in lines:
    w = w.replace(",","")
    m = w.strip()
    parts = m.split()
    list = list + parts  
seq = "NPSLPWTYPPRFYCSKCGNTGYKLKNGRSCKSCWRRFAPQNNVVSAPTYYTNYTMPVYTNAWQGNRPLYVQPGDPRLGGVLCGECRGSGRTRFLLDEDICPLCHGVGR"
for e in list:
    if e in seq:
       print "true"
    else:
       print e

