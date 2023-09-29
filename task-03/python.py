def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
        
def uptoN(n):
    for i in range(2,n+1):
        if isprime(i)==True:
            print(i,end=" ")

n=int(input("enter value of n: "))
uptoN(n)