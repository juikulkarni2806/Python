#Accept Sentence From User and Count the Vowels.
a=input("Please Enter String: ")
count=0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
print (count)


