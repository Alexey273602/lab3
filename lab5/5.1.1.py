import math as m


def solution(a, b):
    y = m.pow(a + 1.5, 1 / 3) + m.pow(a - b, 8) - b / (m.asin(m.pow(a, 2)))
    return y


print(solution(0.3, -21.17))
