
# input
height, width = map(int, input().split())
box = []
for _ in range(height):
    box.append(input())


# main
def search(s):
    path = [(0, -1), s]
    while path:
        now = path[-1]

        next_index = next_state(path[-2], now)
        if is_out(next_index):
            print(len(path) -1)
            return
        else:
            path.append(next_index)

def next_state(p_i, i):
    py,px = p_i
    y, x  = i
    dy = y - py
    dx = x - px
    if box[y][x] == "_":
        return (y + dy, x + dx)
    elif box[y][x] == "\\":
        return (y + dx, x + dy)
    else:
        return (y - dx, x - dy)

def is_out(i):
    y, x = i
    if y < 0 or height <= y:
        return True
    if x < 0 or width <= x:
        return True
    return False


search((0, 0))
