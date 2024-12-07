import random
import sys
import os
import base64
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Використовуємо уєе імплементовану функцію міллера-рабіна з Lab5
from Lab5.miller_rabin import miller_rabin


# Генерація простого числа p
def generate_large_prime(bits=16, k=5):
    while True:
        candidate = random.getrandbits(bits) | 1
        if candidate > 3 and miller_rabin(candidate, k):
            return candidate


# Функція для знаходження первісного кореня
def is_primitive_root(g, p):
    factors = set()
    phi = p - 1  # число Ейлера
    n = phi
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.add(n)
    
    # Перевіряємо, чи є g первісним коренем
    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    return True

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g


class ElGamal:
    def __init__(self, bits=16):
        self.p = generate_large_prime(bits)
        self.g = find_primitive_root(self.p)  # Вибираємо первісний корінь
        self.x = random.randint(1, self.p - 2)  # Приватний ключ
        self.h = pow(self.g, self.x, self.p)  # Відкритий ключ
    
    def encrypt(self, message):
        # Перетворюємо текст у числовий список
        message_numbers = [ord(char) for char in message]
        encrypted_pairs = []
        
        for m in message_numbers:
            y = random.randint(1, self.p - 2)  # Випадкове число
            c1 = pow(self.g, y, self.p)
            c2 = (m * pow(self.h, y, self.p)) % self.p
            encrypted_pairs.append((c1, c2))
        
        return encrypted_pairs

    def decrypt(self, encrypted_pairs):
        decrypted_numbers = []
        
        for c1, c2 in encrypted_pairs:
            s = pow(c1, self.x, self.p)  # Відновлення ключа
            s_inv = pow(s, -1, self.p)  # Мультиплікативна обернена
            m = (c2 * s_inv) % self.p
            decrypted_numbers.append(m)
        
        # Перетворюємо числовий список назад у текст
        decrypted_message = ''.join(chr(num) for num in decrypted_numbers)
        return decrypted_message


# Тестування
if __name__ == "__main__":

    # Генеруємо ключі з простим числом довжини 16 бітів
    elgamal = ElGamal(bits=32)  
    
    print(f"Просте число p: {elgamal.p}")
    print(f"Первісний корінь g: {elgamal.g}")
    print(f"Приватний ключ x: {elgamal.x}")
    print(f"Відкритий ключ h: {elgamal.h}")
    
    # Повідомлення для шифрування
    message = "Hello, World!"  
    print(f"Оригінальне повідомлення: {message}")
    
    encrypted_message = elgamal.encrypt(message)
    print(f"Зашифроване повідомлення: {encrypted_message}")
    
    decrypted_message = elgamal.decrypt(encrypted_message)
    print(f"Розшифроване повідомлення: {decrypted_message}")