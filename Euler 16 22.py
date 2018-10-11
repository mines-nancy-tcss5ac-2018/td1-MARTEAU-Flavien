#Euler 22

f = open("p022_names.txt", "r")
for ligne in f:
    l= ligne.split(',')
L=sorted(l)

def score(k):
    sum=0
    for lettre in L[k]:
        sum+= ord(lettre)-64 
    sum+=60   # "
    return(sum*(k+1))
assert score(937)==49714

total=0
for j in range(len(L)):
    total+=score(j)
    
print( total )  

# Problème 16
def solve(n):
    sum=0
    p=2**n
    while p!=0:
        sum+=p%10
        p=p//10
    return(sum)
assert (solve(15)==26)
print(solve(1000))