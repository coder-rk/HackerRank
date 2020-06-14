# Set Mutations
if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    for i in range(int(input())):
        string = input()
        x = string.split()[0]
        if x == 'intersection_update':
            val = string.split()[1]
            b = set(map(int, input().split()))
            a = a.intersection(b)
        elif x == 'update':
            val = string.split()[1]
            b = set(map(int, input().split()))
            a.update(b)
        elif x == 'symmetric_difference_update':
            val = string.split()[1]
            b = set(map(int, input().split()))
            a = a.symmetric_difference(b)
        elif x == 'difference_update':
            val = string.split()[1]
            b = set(map(int, input().split()))
            a = a.difference(b)
    print(sum(a))
