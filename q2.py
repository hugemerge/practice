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
containers = list(map(int, input().split()))
goal = int(containers[0] / 2)

def bfs(start):
    que = [[start]]
    while que:
        path = que.pop(0)
        now = path[-1]
        for p in now:
            if p == goal:
                print(path)
                return

        for n in next_state(now):
            if n in path:
                continue
            que.append(path + [n])

def next_state(state):
    states = []
    for i,p in enumerate(state):
        if p < 1: continue
        for n in [m for m in [0, 1, 2] if i != m]:
            # p を state[n] に 移動する
            state_updated = state[:]
            orig = p
            move_to = state[n]
            max_move_to = containers[n]
            # check
            if orig > max_move_to - move_to:
                state_updated[i] = orig - (max_move_to - move_to)
                state_updated[n] = max_move_to
            else:
                state_updated[i] = 0
                state_updated[n] = move_to + orig

            states.append(state_updated)

    return states


bfs([containers[0], 0, 0])
