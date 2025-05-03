for num in range(100, 1000):
    # 获取百位数字
    hundreds = num // 100
    # 获取十位数字
    tens = (num // 10) % 10
    # 获取个位数字
    units = num % 10
    # 计算各位数字立方和
    sum_cubes = hundreds ** 3 + tens ** 3 + units ** 3
    if sum_cubes == num:
        print(num, end=' ')