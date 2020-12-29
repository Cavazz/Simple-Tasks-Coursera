#7.2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
i=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        i=i+1
        pos=line.find(":")
        num=line[pos+1:]
        num=float(num)
        count=count+num
        continue
ave=count/i
ave=str(ave)
print("Average spam confidence: " + ave)


#8.4
fname = input("Enter file name: ")
fh = open(fname)
wordlist=list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    wordlist=wordlist+words
wordlist.sort()
main=[]
for element in wordlist:
    if not element in main:
        main.append(element)
    else: continue
print(main)

#8.5
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    else:
        words = line.split()
        print(words[1])
        count+=1

print("There were", count, "lines in the file with From as the first word")

