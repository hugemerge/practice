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

def dfs_recursive(now, goal, path=[]):
    path += [now]
    if now == goal:
        print(path)

    for n in adjacent[now]:
        if n not in path:
            dfs_recursive(n, goal, path)
            path.pop(-1)

def dfs_all(vertex, path=[]):
    path += [vertex]

    for n in adjacent[vertex]:
        if n not in path:
            path = dfs_all(n, path)

    return path

def dfs_non_recursive(start):
    stack, path = [start], [] # stackは処理待ちリスト pathは通過済み頂点のリスト 

    while stack:
        vertex = stack.pop() # remove xX*last*Xx item
        if vertex in path: # 通ったことがあるか
            continue
        path.append(vertex) # 通ってよし
        for n in adjacent[vertex]: # 次に進むところを探す
            stack.append(n)

    return path

def dfs_itr(start, goal):
    stack, path = [start], []
    while stack:
        vertex = stack.pop()
        if vertex not in path:
            path.append(vertex)

            if vertex == goal:
                print(path)

            for n in adjacent[vertex]:
                stack.append(n)

if __name__ == "__main__":
    # dfs_recursive("A", "G")
    # print(dfs_all("A"))
    # print(dfs_non_recursive("A"))
    dfs_itr("A", "G")
