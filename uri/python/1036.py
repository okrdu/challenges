A, B, C = [float(x) for x in input().split()]

delta = B ** 2 - 4 * A * C

if delta < 0 or (A == 0):
    print('Impossivel calcular')
else:
    R1 = (-B + (delta ** (1/2))) / (2 * A)
    R2 = (-B - (delta ** (1/2))) / (2 * A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))
