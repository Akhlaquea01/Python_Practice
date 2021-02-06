def listToString(s):  
    
    str1 = "" 
    
    return (str1.join(s)) 
        
        
# Driver code  

l = []   
a = input('dg: ')
l.append(a)
b = input('dg: ')
l.append(b)
c = input('dg: ')
l.append(c)

print(l)
s=sorted(l)
print(listToString(s))