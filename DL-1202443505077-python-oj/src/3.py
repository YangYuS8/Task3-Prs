m = float (input())
if m<= 1000 :
    a=0
elif m<=3000 :
    a=0.03 * m
elif m<=5000 :
    a=0.04 * m
else  :
    a=0.06 * m
print (a)