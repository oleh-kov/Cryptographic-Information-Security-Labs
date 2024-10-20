
ukrainian_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def generate_cipher_alphabet(keyword, shift, alphabet):
    if not all(ch in alphabet for ch in keyword):
        raise ValueError("Keyword contains characters not present in the alphabet")

    # Позбавляємось дублікатів (оскільки всі символи ключа повинні бути різними)
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    
    # Вставляємо ключ на місце зсуву
    cipher_alphabet = alphabet[:shift] + keyword + alphabet[shift:]
    
    # Позбуваємось дублікатів символів які могли повторюватися
    cipher_alphabet = ''.join(sorted(set(cipher_alphabet), key=cipher_alphabet.index))
    
    # print(f"Keyword: {keyword}, Shift: {shift}, Cipher Alphabet: {cipher_alphabet}\n")
    return cipher_alphabet


def encrypt(text, keyword, shift, alphabet=ukrainian_alphabet):
    
    cipher_alphabet = generate_cipher_alphabet(keyword, shift, alphabet)
    
    # Мапимо текст до шифротексту
    encrypt_map = {alphabet[i]: cipher_alphabet[i] for i in range(len(alphabet))}
    
    # Шифруємо текст
    encrypted_text = ''.join([encrypt_map.get(ch, ch) for ch in text.lower()])
    
    return encrypted_text


def decrypt(text, keyword, shift, alphabet=ukrainian_alphabet):
    cipher_alphabet = generate_cipher_alphabet(keyword, shift, alphabet)
    
    # Мапимо текст до шифротексту
    decrypt_map = {cipher_alphabet[i]: alphabet[i] for i in range(len(alphabet))}
    
    # Дешифруємо текст
    decrypted_text = ''.join([decrypt_map.get(ch, ch) for ch in text.lower()])
    
    return decrypted_text


# Приклад використання
keyword = "програмне"  
shift = 3
plaintext = "забезпечення"

encrypted = encrypt(plaintext, keyword, shift)
decrypted = decrypt(encrypted, keyword, shift)

print("Original text: ", plaintext)
print("Encrypted text: ", encrypted)
print("Decrypted text: ", decrypted)