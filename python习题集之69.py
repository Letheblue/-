"""
题目：有 n 个人围成一圈，顺序排号。
从第一个人开始报数（从 1 到 3 报数），凡报到 3
的人退出圈子，问最后留下的是原来第几号的那位。
"""
n = int(input("请输入围成一圈的人数："))
list2 = [i for i in range(1, n + 1)]       # 一个存储所有人数的列表
j, k = len(list2), 0    
while j > 1:        # 判断列表中是否只剩下一个人
    list2 = [i for i in list2 if (list2.index(i)+k+1) % 3 != 0]     # 留下报数没有数到3的人
    k = (j + k) % 3 
    j = len(list2)
print(list2)    # 打印留下来的那个人
