import random
import sys
import os

# Додаємо батьківську директорію до sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab5_not_completed.miller_rabin import miller_rabin
from Lab4.evklid import gcdex

def generate_prime(bits):
    """Генерує просте число заданої бітової довжини."""
    attempts = 0
    while attempts < 1000:  # Обмежуємо кількість спроб
        num = random.getrandbits(bits)
        if num % 2 == 0:
            num += 1
        if num > 3 and miller_rabin(num, 40) == f"Ймовірно просте число з ймовірністю {1 - (1/4)**40:.4f}":
            return num
        attempts += 1
    raise ValueError("Не вдалося згенерувати просте число після 1000 спроб")

def generate_keys(bits):
    """Генерує пару ключів RSA."""
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Вибираємо відкритий ключ e
    e = 65537  # базове значення
    
    # Знаходимо закритий ключ d (з використанням розширеного алгоритму Евкліда, згідно умови завдання ^_^)
    _, d, _ = gcdex(e, phi)
    d = d % phi  # вибираємо закритий ключ d такий, що d позитивне
    
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Шифрує повідомлення за допомогою відкритого ключа."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    """Розшифровує шифротекст за допомогою закритого ключа."""
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Тестування
if __name__ == "__main__":
    try:
        public_key, private_key = generate_keys(1024)
        message = "Привіт світ" 
        
        print(f"Відкритий ключ: {public_key}")
        print(f"Закритий ключ: {private_key}")
        print(f"Оригінальне повідомлення: {message}")
        
        encrypted = encrypt(message, public_key)
        print(f"Зашифроване повідомлення: {encrypted}")
        
        print(len(encrypted), "байтів зашифрованого повідомлення (кількість елементів зашифрованого повідомлення)")
        decrypted = decrypt(encrypted, private_key)
        print(f"Розшифроване повідомлення: {decrypted}")
        
        assert message == decrypted, "Помилка: розшифроване повідомлення не співпадає з оригінальним!"
        print("Успішно: шифрування та розшифрування працює коректно.")
    except Exception as e:
        print(f"Виникла помилка: {e}")