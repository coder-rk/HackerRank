# The Captain's Room
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    c = Counter(map(int, input().split()))
    d = dict(c)
    for i, j in d.items():
        if j == 1:
            print(i)
            break
