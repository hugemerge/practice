
# input
height, width = map(int, input().split())
box = ""
for _ in range(height):
    box += input()


# main
def search(s):
    path = [-1, s]
    while path:
        now = path[-1]

        next_index = next_state(now, path[-2])
        if is_out(now, next_index):
            print(len(path) -1)
            return
        else:
            path.append(next_index)

def next_state(i, p_i):
    if box[i] == "_":
        return i + (i - p_i)
    elif box[i] == "\\":
        d = i - p_i
        if abs(d) == 1:
            return i + width * d
        elif d < 0:
            return i - 1
        else:
            return i + 1
    else:
        d = i - p_i
        if abs(d) == 1:
            return i + width * d * -1
        elif d < 0:
            return i + 1
        else:
            return i - 1

def is_out(i, next_i):
    d = next_i - i
    if i < width and d == width * -1:
        return True
    if width * (height - 1) <= i and d == width:
        return True
    if i % width == 0 and d == -1:
        return True
    if i % width == width - 1 and d == 1:
        return True

    return False


search(0)
