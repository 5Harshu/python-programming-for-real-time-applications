l=[9,3,734,83,75,19,23,53,45,60]
def sumsquare(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    l=[odd,even]
    return(l)
print(sumsquare(l))
