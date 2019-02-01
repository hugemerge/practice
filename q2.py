"""
https://qiita.com/NotFounds/items/4707bacd5934f6191c9d#%E5%95%8F%E9%A1%8C%E6%A6%82%E8%A6%81

ユウキ君は8dLのピッチャーに入ったヨーグルトスムージーをレイちゃんと半分にする方法を考えています。
ユウキ君は8dL、5dL、3dL入るピッチャーを使うことができます。
スムージーを最低何回移し替えればいいでしょうか？

[input]
8 5 3

[output]
N
"""

# Answer

# input
containers = map(int, input().split())

def dfs(start):
    que = [[start, 0, 0]]
    while que:
        path = que.pop()
        now = path[-1]
        if now == int(start / 2):
            print(path)

        for n in containers:
            que.append(n)
