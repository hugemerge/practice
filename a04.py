# input
length, n, m = map(int, input().split())
lines = []
for _ in range(m):
    a,b,c = map(int, input().split())
    lines.append([a-1, b, c])

nodes = [[0]*n for _ in range(length+1)]
for line in lines:
    left_i, l_y, r_y = line
    # left -> right
    nodes[l_y][left_i] = (r_y, left_i+1)

    # right -> left
    nodes[r_y][left_i+1] = (l_y, left_i)


# main
def amida(start):
    path = [start]
    while True:
        now = path[-1]
        if now[0] == 0:
            print(now[1] + 1)
            return

        next_index = next_state(now)
        path.append(next_index)

def next_state(i):
    y,x = i
    if nodes[y][x]:
        n_y,n_x = nodes[y][x]
        return (n_y-1, n_x)
    else:
        return (y-1, x)

amida((length, 0))
