#loops
dd={'hi':1,'five':5,'zeg':6,'meg':7}
for i in range(10):
    print(i+5)

for j in range(len('shivani')):
    print (j+1,'shivani'[j])

for n in ['apple','mango','orange','gauva','lime']:
    if(n=='orange'):
        print("found",n,"in nagpur")
    else:
        print("NA",n)

for k in dd:
    print (k,dd[k])

i1=13
while True:
    print('*',i1,'*')
    i1=i1+1
    if(i1>9):
        print("*",i1,"*")
        break

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=" ")
    print("")