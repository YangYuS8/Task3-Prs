m = int (input())
if m <=4 :
    s=50
elif m<=8 :
    s=50 +(m-4)*20
else :
    s=50 +4 *20+(m-8)*30
print(s)