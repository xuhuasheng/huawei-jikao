# 题目描述
# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

# 输入描述:
# 输入一个int型整数

# 输出描述:
# 按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

# 示例1
# 输入
# 复制
# 9876673
# 输出
# 复制
# 37689

s = "2752771"
# s = input()
n = list(s)
s = set()
res = []
for i in range(len(n)-1, -1, -1):
    if n[i] not in s:
        s.add(n[i])
        res.append((n[i]))
print(''.join(res))

# 1.概念：Python中的集合和数学上的集合是一致的

# 特点：set中不会存储重复的元素，可以进行交集，并集或者差集运算
# 缺点：set和dict类似，set相当于值存储了key的集合
# 本质：无序且无重复元素的集合

# 2.创建 ：集合名 = set（list/tuple/dict）
# 注意： 重复元素在set中会被自动过滤掉，重复元素在set中会被自动过滤掉

# 3.操作 

# a）add()：元素添加为集合中没有的元素
# b） remove()：s3.remove（被删除元素），只能用于元素的删除，不用于索引的删除

# c）交集和并集： &【按位与】 和 |【按位或】