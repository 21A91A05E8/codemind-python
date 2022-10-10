s=input()
for i in range(len(s)):
    if s[i]=='6':
        print(s[:i]+'9'+s[i+1:])    
        exit()
print(s)        