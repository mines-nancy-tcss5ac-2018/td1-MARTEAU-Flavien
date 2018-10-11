def inverse(n) :
    m = str(n)
    inv = str()
    for letter in m :
        inv = letter + inv
    return(int(inv))
    
def lychrel(n):
    for k in range(49):
        n+=inverse(n)
        if n==inverse(n):
           return(False)
    return(True)            
assert(lychrel(196))
            
c=0
for k in range(1,10000):
    if lychrel(k):
        c+=1
print(c)