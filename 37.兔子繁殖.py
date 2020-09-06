# 题目描述
# 有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？

# 输入描述:
# 输入int型表示month

# 输出描述:
# 输出兔子总数int型

# 示例1
# 输入
# 复制
# 9
# 输出
# 复制
# 34

while True:
    try:
        m = int(input())
        k3 = 0
        k2 = 0
        k1 = 1
        for i in range(m-1):
            k3 = k3 + k2
            k2 = k1
            k1 = k3
        print(k1+k2+k3)
    except:
        break