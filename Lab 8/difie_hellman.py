import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Використовуємо уєе імплементовану функцію міллера-рабіна з Lab5
from Lab5.miller_rabin import miller_rabin


def generate_secure_prime(bits, k=5):
    while True:
        q = random.getrandbits(bits - 1)
        if miller_rabin(q, k) == "Ймовірно просте число з ймовірністю 0.9990":
            p = 2 * q + 1
            if miller_rabin(p, k) == "Ймовірно просте число з ймовірністю 0.9990":
                return p

# Функція щоб знайти генератор g для Z_p
def find_generator(p):
    for g in range(2, p):
        if pow(g, (p - 1) // 2, p) != 1:
            return g
    return None

# Алгоритм Діффі-Хеллмана
def diffie_hellman_key_exchange(bits=512):

    # Генеруєм безпечне просте p
    p = generate_secure_prime(bits)
    print(f"\n\nЗгенероване безпечне просте (p): {p}\n\n")

    # Шукаємо генератор g
    g = find_generator(p)
    print(f"Генератор (g): {g}\n\n")

    # Секретний ключ Аліси
    a = random.randint(2, p - 2)
    print(f"Секретний ключ Аліси (a): {a}\n\n")

    # Секретний ключ Боба
    b = random.randint(2, p - 2)
    print(f"Секретний ключ Боба (b): {b}\n\n")

    # Приватний ключ Аліси
    A = pow(g, a, p)
    print(f"Приватний ключ Аліси (A): {A}\n\n")

    # Приватний ключ Боба
    B = pow(g, b, p)
    print(f"Приватний ключ Боба (B): {B}\n\n")

    # Спільний секрет
    shared_secret_alice = pow(B, a, p)
    print(f"Спільний секрет Аліси (Alice): {shared_secret_alice}\n\n")

    shared_secret_bob = pow(A, b, p)
    print(f"Спільний секрет Боба (Bob): {shared_secret_bob}\n\n")

    assert shared_secret_alice == shared_secret_bob, "Неудача! Спільний секрет не співпадає!"
    return shared_secret_alice

# Тестимо
def test_diffie_hellman():
    shared_secret = diffie_hellman_key_exchange()
    print("Спільний секрет:", shared_secret)

if __name__ == "__main__":
    test_diffie_hellman()