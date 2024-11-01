# Завдання №3

def phi(m):
    count = 0
    for i in range(1, m):
        if gcd(i, m) == 1:
            count += 1
    return count

def gcd(a, b):
    """
    Обчислює НСД a та b.
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # Приклад використання
    m = 154
    result = phi(m)
    print(f"Функція Ейлера phi({m}) = {result}")
