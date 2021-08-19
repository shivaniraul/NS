n1=int(input())
a=int(input())
b=int(input())
def func1():
    print("Enter your name")
    name=input()
func1()

def func2(snme):
    print(snme)
func2('Raj')
func2('Shreya')

def eo(n1):
    for i in range(2,n1):
        if i%2==0:
            print(i," is Even No")
        else:
            print(i,"is ODD")
eo(n1)    

def fun3(val):
    return 5*val
fun3(4)
print(fun3(6))

def maxn(a,b):
    if a>b:
        return print(a)
    else:
        return print(b)
maxn(a,b)

