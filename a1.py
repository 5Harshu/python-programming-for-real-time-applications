def anil(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(anil("fool","poor"))
print(anil("foal","poor"))
print(anil("too","bar"))
print(anil("toto","yaya"))
