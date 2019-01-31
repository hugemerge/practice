import random

def nibu(cards_sorted, target):

    i = int(len(cards_sorted) / 2)
    be = i
    for _ in range(i):
        center = cards_sorted[i]
        if center == target:
            print(i, "t:", target)
            break
        elif center > target:
            be = i
            i = max(be, i)

def binary_search(cards_sorted, target):
    print("cards: ", cards_sorted)
    low = 0
    high = len(cards_sorted) - 1
    while low <= high:
        mid = (low + high) // 2
        center = cards_sorted[mid]
        if center == target:
            print("index of target is {}".format(mid+1))
            break
        elif center < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("None")
    return

if __name__ == "__main__":
    cards = list(range(1, 14))
    def ram(n=13):
        return random.sample(cards, n)
    for _ in range(5):
        binary_search(sorted(ram(random.randint(0, 13))), 8)
