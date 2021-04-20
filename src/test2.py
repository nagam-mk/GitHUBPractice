s1=input('Enter string 1:')
s2=input('Enter string 2:')
s3=''
i=0
while i<len(s1):
    s3=s3+s1[i]+s2[i]
    i=i+1
print(s3)
#--------------------------------
s1=input('Enter string 1:')
s2=input('Enter string 2:')
s3=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        s3=s3+s1[i]
        i=i+1
    if j<len(s2):
        s3=s3+s2[j]
        j=j+1
print('The final string:',s3)

