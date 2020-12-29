import re
hand = open('regex_sum_796277.txt')
s=0
count=0
for line in hand:
    line=line.rstrip()
    x = re.findall('[0-9]+',line)
    for num in x:
        h=int(num)
        count=count+1
        s=s+h
print(count)
print(s)
