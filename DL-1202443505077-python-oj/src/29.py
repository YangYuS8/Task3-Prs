n = int (input())
i=n
a=0
while i>0:
    a+=i%10
    i//=10
print (a)