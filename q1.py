"""
列の数がm、行の数がnのマスで構成される迷路がある。
迷路の各マスはスタート(s)、ゴール(g)、通行可能なマス(0)、通行不可能なマス(1)のいずれかの状態である。
スタート(s)から出発し上下左右に1マスずつ通行可能なマス(0)のみ通りゴール(g)まで移動した場合の、最短歩数を求めよ。

[入力]
1行目には列の数mと行の数nがスペース区切りで入力される。
2行目以降は、m個の文字がスペース区切りでn行入力される。
2行目以降に入力される文字は s/g/0/1 のいずれかであり、他の文字が入力されることは考慮しなくて良い。

[出力]
最短歩数を一行で出力する。(>> 経路を出力)
ただしゴールにたどり着けない場合は「-1」を出力する。

[example]
5 6
s 0 0 0 0
0 0 1 0 0
0 1 0 0 0
0 0 g 1 0
0 0 0 0 0
0 0 1 0 0
"""

# Answer

# input
width, height = map(int, input().split())
vertex = []
for _ in range(height):
    for v in input().split():
        vertex.append(v)

start = vertex.index("s")
goal = vertex.index("g")

def move_to(i):
    available = []
    if i < width * (height-1):
        available.append(i + width)
    if width <= i:
        available.append(i - width)
    if i % width != 0:
        available.append(i - 1)
    if i % width != width-1:
        available.append(i + 1)

    return available

def bfs(s):
    que = [[s]]
    while que:
        path = que.pop(0)
        now = path[-1]
        if now == goal:
            print(path)
            return

        for n in move_to(now):
            if vertex[n] == "1":
                continue
            if n not in path:
                que.append(path + [n])

    print(-1)

bfs(start)
