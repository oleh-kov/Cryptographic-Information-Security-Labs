def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

# SHA-1 функція
def sha1(message):
    # Препроцесування: додавання відступу до повідомлення
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    message += original_bit_len.to_bytes(8, byteorder='big')

    # Ініціалізація хешу
    h0, h1, h2, h3, h4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0

    # Обробка повідомлення в частини 512 біт
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = [0] * 80
        for j in range(16):
            w[j] = int.from_bytes(chunk[j*4:(j*4)+4], byteorder='big')
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        # Головний цикл SHA-1
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Додаємо раніше отримані хеші цього фрагмента до отриманого результату:
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Отримуємо фінальне хеш-значення як 160-бітове число
    return b''.join(x.to_bytes(4, byteorder='big') for x in [h0, h1, h2, h3, h4])

# Тест SHA-1
def test_sha1():
    # Тестові значення (взяті з онлайн калькулятора ^_^)
    test_cases = [
        (b"", "da39a3ee5e6b4b0d3255bfef95601890afd80709"),
        (b"a", "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"),
        (b"abc", "a9993e364706816aba3e25717850c26c9cd0d89d"),
        (b"message digest", "c12252ceda8be8994d5fa0290a47231c1d16aae3"),
        (b"abcdefghijklmnopqrstuvwxyz", "32d10c7b8cf96570ca04ce37f2a19d84240d3a89")
    ]
    for message, expected_hash in test_cases:
        result = sha1(message).hex()
        print(f"SHA-1(\"{message.decode('utf-8')}\") = {result}")
        assert result == expected_hash
    print("Всі тести пройшли успішно!")

if __name__ == "__main__":
    test_sha1()
