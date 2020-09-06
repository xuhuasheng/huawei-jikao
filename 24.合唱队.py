# 题目描述
# 计算最少出列多少位同学，使得剩下的同学排成合唱队形

# 说明：

# N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
# 合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。

# 你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。


# 注意不允许改变队列元素的先后顺序
# 请注意处理多组输入输出！

# 输入描述:
# 整数N

# 输出描述:
# 最少需要几位同学出列

# 示例1
# 输入
# 复制
# 8
# 186 186 150 200 160 130 197 200
# 输出
# 复制
# 4

# 思路:

# 　　求两次最长递增子序列，先从左往右求递增子序列a[n]，采用动态规划的方法，具体见代码。再求从右到左的递增子序列b[n]。

# 　　

# 　　假设输入为:

# 　　　　　　 186 186 150 200 160 130 197 200
# 　　　　a[n]  1  1   1   2    2  1   3   4  从左到右
# 　　　　b[n]  3  3   2   3    2  1   1   1  从右到左
# 　　　　c[n]  4  4   3   5    4  2   4   5
# 　　取c[i]最大值 5, i = 3; 所以包括3这个位置左边有2个是合唱队列的，包括3这个位置右边有3个是合唱队列的。
# 　　由于3被计算了2次，所以合唱队列为:2+3-1 = 4人。
# 　　由于总人数为:8 , 所以需要抽出8-4人。
import sys

def LIS(arr):
    dp = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def LIS_left(arr):
    dp = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

def LIS_right(arr):
    dp = [1] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        for j in range(i+1, len(arr)-1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

# 时间复杂度:o(nlogn)
import bisect
def deal(arr):
    d = []
    count = []
    for val in arr:
        if not d: # 选中队列中的一个学生，以该学生为核心
            d.append(val)
            count.append(1)
        elif d[-1] < val:
            d.append(val)
            count.append(count[-1]+1)
        else:
            d[bisect.bisect_left(d, val)] = val
            count.append(count[-1])
    return count

if __name__ == "__main__":
    # # 打开输入文件
    # f = open("0.inputfile.txt", "r")
    # # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    # sys.stdin = f
    # arr = list(map(int, input().split(' '))
    arr = [186,186, 150, 200, 160, 130, 197, 200]
    left_inc = LIS_left(arr)
    right_inc = LIS_right(arr)
    res = 0
    for i in range(len(arr)):
        res = max(res, left_inc[i] + right_inc[i] - 1)
    print(len(arr) - res)
