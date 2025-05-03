# 循环01
# 输入一批正整数(假设个数<100)，输入0时结束循环，找出其中最大的数
max_num = float('-inf')
while True:
    nums_str = input()
    if nums_str == '0':
        break
    # 将输入的字符串按空格分割成列表
    nums_list = nums_str.split()
    for num_str in nums_list:
        num = int(num_str)
        if num > max_num:
            max_num = num
print(max_num)