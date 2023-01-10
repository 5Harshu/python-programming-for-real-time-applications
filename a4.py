def onedigit(num):
      return((num>=0) and (num<10))
def anilreddy(num,dupnum):
      if onedigit(num):
            return(num==(dupnum[0])%10)
      if not anilreddy(num//10,dupnum):
            return False
      dupnum[0]=dupnum[0]//10
      return (num%10==(dupnum[0])%10)
def anil(num):
      if (num<0):
            num=-num
      dupnum=[num]
      return anilreddy(num,dupnum)
n=1234321
if  anil(n):
      print('yes')
else:
      print('no')

      
