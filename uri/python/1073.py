value = int(input())

for i in range(1, value+1):
    if i % 2 == 0:
        print('{0}^2 = {1}'.format(i, i ** 2))
