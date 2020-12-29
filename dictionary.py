#9.4

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
adres=list()
for line in handle:
    line.rstrip()
    if not line.startswith('From '): continue
    else:
        words = line.split()
        adres.append(words[1])
for i in adres:
    if i not in counts:
        counts[i]=1
    else:
        counts[i]=counts[i]+1
bigcount = None
bigword = None
for i,adres in counts.items():
    if bigcount is None or adres > bigcount:
        bigword = i
        bigcount = adres
print(bigword, bigcount)
#10.2
# key is hour
# value is number of messages

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
d = dict()
adres = list()
final = list()
for line in handle:
    line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        adres.append(words[5])
for i in adres:
    i.rstrip()
    hrs = i.split(":")
    final.append(hrs[0])
for h in final:
    d[h] = d.get(h, 0) + 1

for k, v in sorted(d.items()):
    print(k, v)
