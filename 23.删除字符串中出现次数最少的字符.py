# 题目描述
# 实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
# 注意每个输入文件有多组输入，即多个字符串用回车隔开
# 输入描述:
# 字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

# 输出描述:
# 删除字符串中出现次数最少的字符后的字符串。

# 示例1
# 输入
# 复制
# abcdd
# 输出
# 复制
# dd
def func(ss):
    s = list(ss)
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    min_cnt = min(d.values())
    res = []
    for i in s:
        if d[i] != min_cnt:
            res.append(i)
    return ''.join(res)
        
import sys
if __name__ == "__main__":
    # 打开输入文件
    f = open("0.inputfile.txt", "r")
    # 把标准输入流重定向到文件(默认是键盘输入缓冲区)
    sys.stdin = f
    while True:
        try:
            s = input()
            print(func(s))
        except:
            break