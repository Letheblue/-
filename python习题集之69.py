n = int(input("请输入围成一圈的人数："))
list2 = [i for i in range(1, n + 1)]
j, k = len(list2), 0
while j > 1:
    list2 = [i for i in list2 if (list2.index(i)+k+1) % 3 != 0]
    k = (j + k) % 3
    j = len(list2)
print(list2)
