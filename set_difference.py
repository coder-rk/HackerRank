# Set .difference() Operation
if __name__ == '__main__':
    n = int(input())
    a = set(list(map(int, input().split())))
    m = int(input())
    b = set(list(map(int, input().split())))
    print(len(a.difference(b)))
