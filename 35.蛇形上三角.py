# 题目描述
# 题目说明
# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
# 样例输入
# 5
# 样例输出
# 1 3 6 10 15
# 2 5 9 14
# 4 8 13
# 7 12
# 11
# 输入描述:
# 输入正整数N（N不大于100）
# 输出描述:
# 输出一个N行的蛇形矩阵。
# 示例1
# 输入
# 复制
# 4
# 输出
# 复制
# 1 3 6 10
# 2 5 9
# 4 8
# 7

while True:
    try:
        N = int(input())
        head = 1
        for i in range(N):
            head += i
            add = i+2
            tmp = head
            for j in range(N-i):
                if j == 0:
                    print(tmp, end=' ')
                else:
                    print(tmp + add, end=' ')
                    tmp = tmp + add
                    add += 1
                if j == N-i-1:
                    print()
    except:
        break

# # include <bits/stdc++.h>
# using namespace std;

# int main() {
#     int n;
#     while (cin>>n) {
#         int head = 1;
#         for (int i = 1; i<=n; ++i) {
#             head += (i-1);
#             int temp = head;
#             int add = i+1;
#             for (int j=1; j<=(n-i+1); ++j) {
#                 if (j==1) cout<<temp<<' ';
#                 else {
#                     cout<<(temp+add)<<' ';
#                     temp = temp + add;
#                     add += 1;
#                 }
#                 if (j==(n-i+1)) cout<<endl;
#             }
#         }
#     }
#     return 0;
# }
