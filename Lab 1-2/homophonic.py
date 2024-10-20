import random

alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ !?,.-'

# Створення таблиці шифрування з тризначними числами
def generate_cipher_table(alphabet, num_options=3):
    cipher_table = {}
    all_numbers = list(range(100, 1000))
    random.shuffle(all_numbers)
    
    for letter in alphabet:
        cipher_table[letter] = [all_numbers.pop() for _ in range(num_options)]
    
    return cipher_table

# Шифрування
def encrypt(text, cipher_table):
    encrypted_text = ""
    for char in text.upper():
        if char in cipher_table:
            encrypted_text += str(random.choice(cipher_table[char]))
    return encrypted_text

# Дешифрування
def decrypt(encrypted_text, cipher_table):
    decrypted_text = ""
    # Розбиваємо за тризначними числами
    for i in range(0, len(encrypted_text), 3):
        num = int(encrypted_text[i:i+3])
        # print(f"num= {num}")
        # Шукаємо в таблиці відповідну літеру
        for letter, codes in cipher_table.items():
            if num in codes:
                decrypted_text += letter
                break
    return decrypted_text


cipher_table = generate_cipher_table(alphabet)
print("Шифрувальна таблиця: ", cipher_table)

text = "СЛАВА УКРАЇНІ!"
encrypted = encrypt(text, cipher_table)
decrypted = decrypt(encrypted, cipher_table)

print(f"Оригінал: {text}")
print(f"Зашифрований текст: {encrypted}")
print(f"Розшифрований текст: {decrypted}")
