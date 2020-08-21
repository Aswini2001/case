letter = input ("write a string")
count=0
lcount=0
for x in letter:
    if(x.islower()):
        count=count+1
    elif(x.isupper()):
        lcount=lcount+1
print("NO.OF.UPPERCASE: "+str(lcount))
print("NO.OF LOWERCASE:: "+str(count))
