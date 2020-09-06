s = input().lower()
k = input().lower()
# print(s.count(k))
cnt = 0
for i in s:
    if i == k:
        cnt+=1
print(cnt)