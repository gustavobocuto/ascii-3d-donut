import math
import time
import sys

A = 0
B = 0

print("\x1b[2J")  # Limpa a tela uma vez no início

while True:
    z = [0] * 1760
    b = [' '] * 1760

    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= o < 1760 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[max(0, N)]

    sys.stdout.write('\x1b[H')  # Move o cursor pro topo
    for i in range(0, 1760, 80):
        sys.stdout.write(''.join(b[i:i+80]) + '\n')
    sys.stdout.flush()

    A += 0.04
    B += 0.08
    time.sleep(0.05)
