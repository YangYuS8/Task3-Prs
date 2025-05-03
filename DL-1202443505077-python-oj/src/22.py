#输入一个正整数num，判断num是否为素数。若为素数则输出1，否则输出0。（提示：素数是指只可以被1和其本身整除的正数（1除外））
#输入10输
#输入7输出1
num = int(input())
if num < 2:
    print(0)
else:
    a =True
    for i in range(2,int(num**0.5)+1):
        if num %i == 0:
            a = False
            break
    if a:
        print(1)
    else:
        print(0)   