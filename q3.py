"""
たかはし君は迷路が好きです。今、上下左右に移動できる二次元盤面上の迷路を解こうとしています。盤面は以下のような形式で与えられます。

まず、盤面のサイズと、迷路のスタート地点とゴール地点の座標が与えられる。
次に、それぞれのマスが通行可能な空きマス(.)か通行不可能な壁マス(#)かという情報を持った盤面が与えられる。
盤面は壁マスで囲まれている。
スタート地点とゴール地点は必ず空きマスであり、スタート地点からゴール地点へは、空きマスを辿って必ずたどり着ける。具体的には、入出力例を参考にすると良い。

[入力]
入力は以下の形式で標準入力から与えられる。

R C
sy sx
gy gx
c(1,1)c(1,2) … c(1,C)
c(2,1)c(2,2) … c(2,C)
:
c(R,1)c(R,2) … c(R,C)
1 行目には、行数 R(1≦R≦50)と列数 C(1≦C≦50)がそれぞれ空白区切りで与えられる。
2 行目には、スタート地点の座標 (sy,sx) が空白区切りで与えられる。スタート地点が sy 行 sx 列にあることを意味する。 1≦sy≦R　かつ 1≦sx≦C である。
3 行目には、ゴール地点の座標 (gy,gx) が空白区切りで与えられる。ゴール地点が gy 行 gx 列にあることを意味する。 1≦gy≦R　かつ 1≦gx≦C であり、(gy,gx)≠(sy,sx)であることが保障されている。
4 行目から R 行、長さ C の文字列が 1 行ずつ与えられる。各文字は . もしくは # のいずれかであり、i 回目 (1≦i≦R) に与えられられる文字列のうち j 文字目 (1≦j≦C) について、その文字が . なら、マス (i,j) が空きマスであり、# なら、マス (i,j) が壁マスであることをあらわす。
盤面は壁マスで囲まれている。つまり、i=1,i=R,j=1,j=C のうちいずれか1つでも条件を満たすマス (i,j) について、c(i,j) は #である。また、スタート地点とゴール地点は必ず空きマスであり、スタート地点からゴール地点へは、空きマスを辿って必ずたどり着ける。
[出力]
スタート地点からゴール地点に移動する最小手数を 1 行に出力せよ。最後に改行を忘れないこと。

入力例
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########

出力例
11

"""

# Answer

# input
r, c = map(int, input().split())
s_y, s_x = map(int, input().split())
g_y, g_x = map(int, input().split())
maze = []
for _ in range(r):
    maze.append(input())

# main
start = (s_y-1, s_x-1)
goal = (g_y-1, g_x-1)

def bfs(s):
    que = [[s]]
    while que:
        path = que.pop(0)
        now = path[-1]
        if now == goal:
            print(path)
            print(len(path) - 1)
            return

        for n in go_to_next(now):
            n_y, n_x = n
            if maze[n_y][n_x] == "#":
                continue
            if n not in path:
                que.append(path + [n])

def go_to_next(y_x):
    y, x = y_x
    return [(y, x+1), (y, x-1), (y-1, x), (y+1, x)]


# output
bfs(start)
