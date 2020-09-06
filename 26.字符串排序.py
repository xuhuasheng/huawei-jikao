# 题目描述
# 编写一个程序，将输入字符串中的字符按如下规则排序。

# 规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
# 如，输入： Type 输出： epTy

# 规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
# 如，输入： BabA 输出： aABb

# 规则 3 ：非英文字母的其它字符保持原来的位置。
# 如，输入： By?e 输出： Be?y
# 注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）

# 输入描述:
# 输入字符串
# 输出描述:
# 输出字符串
# 示例1
# 输入
# 复制
# A Famous Saying: Much Ado About Nothing (2012/8).
# 输出
# 复制
# A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).

while True:
    try:
        s = input()
        a = ''
        for i in s:
            # 检测字符串是否只由字母组成
            if i.isalpha():
                a += i
        # 排序依据key为字符串全部转为大写
        b = sorted(a, key=str.upper)
        index = 0
        d = ''
        for i in range(len(s)):
            if s[i].isalpha():
                d += b[index]
                index += 1
            else:
                d += s[i]
        print(d)
    except:
        break

# # include <iostream>
# # include <string>
# # include <vector>
# using namespace std;

# string String_Sorting(string str) {
#     int len = str.length();
#     vector<char> vec;
#     for(int j=0; j<26; ++j) {
#         for (int i=0; i<len; ++i) {
#             if ((str[i]-'a' == j) || (str[i]-'A'==j)) {
#                 vec.push_back(str[i]);
#             }
#         }
#     }
#     for(int i = 0,k = 0;(i < len) && (k < vec.size()); i++)
#     {
#         if((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z'))
#         {
#             str[i] = vec[k++];
#         }
#     }
#     return str;
# }
# int main() {
#     string str;
#     while (cin>>str) {
#         cout<<String_Sorting(str)<<endl;
#     }
#     return 0;
# }