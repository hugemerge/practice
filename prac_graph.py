"""
 /B--D--F
A |  |
 \C--E--G
"""

adjacent = {
    "A": ("B", "C"),
    "B": ("A", "C", "D"),
    "C": ("B", "E"),
    "D": ("B", "E", "F"),
    "E": ("C", "D", "G"),
    "F": ("D",),
    "G": ("E",)
}

def df_search(goal, path): # pathはこれまでの経路のリスト path[-1]:現在地
    now = path[-1]
    if now == goal:
        print(path)

    for n in adjacent[now]:
        if n not in path:
            path.append(n)
            df_search(goal, path)
            path.pop(-1)

def df_search2(goal, path):
    if path[-1] == goal:
        print(path)

    for x in adjacent[path[-1]]:
        if x not in path:
            df_search2(goal, path + [x])

def bf_search(start, goal):
    que = [[start]]
    while len(que) > 0:
        path = que.pop(0)
        n = path[-1]
        if n == goal:
            print(path)

        for x in adjacent[n]:
            if x not in path:
                new_path = path[:]
                new_path.append(x)
                que.append(new_path)

def bf_search2(start, goal):
    que = [[start]]
    while len(que) > 0:
        path = que.pop(0) # ロケット鉛筆!!!
        now = path[-1]
        if now == goal:
            print(path)
        else:
            for x in adjacent[now]:
                if not x in path:
                    que.append(path + [x])
                print(path)


if __name__ == "__main__":
    # df_search("G", ["A"])
    bf_search2("A", "G")
