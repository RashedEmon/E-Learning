# n, x = [int(x) for x in input().split()]
# ans = 0
# for i in range(1, n+1):
#     if x % i == 0:
#         if x/i <= n:
#             ans += 1
# print(ans)

n = int(input())

a = [int(i) for i in input().split()]


def indecrease(arr: list):
    prevCount = 0
    incnt = 0
    max = arr[0]
    deccnt = 0

    for index, i in enumerate(arr):
        if i > max:
            max = i
            incnt += 1
            prevCount = deccnt
            deccnt = 0

        elif i < max:
            deccnt += 1
            prevCount = incnt
            incnt = 0

        print(
            f'in value {i}.increment count:{incnt} and decrement count:{deccnt} max {max}')


indecrease(a)
