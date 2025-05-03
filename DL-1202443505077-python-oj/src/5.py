#编写一个程序，输入一个正整数表示学生的学习成绩，若学习成绩小于0或大于100，输出illegal，否则若成绩在90~100分之间，输出'A'，在60-89分之间的，输出'B'，60分以下的输出'C'。
#输入90 输出A
#输入70 输出B
#输入59 输出C
#输入120 输出illegal
m = int (input ())
if (m>100) or  (m<0) :
    print("illegal")
elif (m>=90) and (m<=100):
    print ("A")
elif (m>=60) and (m<=89):
    print ("B")
elif m<60:
    print ("C")