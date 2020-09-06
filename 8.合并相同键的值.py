# 题目描述
# 数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

# 输入描述:
# 先输入键值对的个数
# 然后输入成对的index和value值，以空格隔开

# 输出描述:
# 输出合并后的键值对（多行）

# 示例1
# 输入
# 复制
# 4
# 0 1
# 0 2
# 1 2
# 3 4
# 输出
# 复制
# 0 3
# 1 2
# 3 4

n = int(input())
dic = {}
for _ in range(n):
    a, b = map(int, input().split(' '))
    if a not in dic:
        dic[a] = b 
    else:
        dic[a] += b 
# sorted()默认是对字典的键，从小到大进行排序
d = sorted(dic)
for k in dic:
    print('{} {}'.format(k, dic[k]))


# 字典的遍历
# for key in d: 和 for key in d.keys():完全等价
# for value in d.values():
# for (k, v) in a.items():
