# Завдання №1

def gcdex(a, b):
    """
    Реалізація ітераційного розширеного алгоритму Евкліда.
    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


if __name__ == "__main__":
    a, b = 612, 342
    gcd, x, y = gcdex(a, b)
    print(f"\ngcd({a}, {b}) = {gcd}\n-----------\nx = {x}, y = {y}")
    print(f"-----------\n{a} * {x} + {b} * {y} = {gcd}")
