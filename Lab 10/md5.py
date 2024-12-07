import math

# Константи MD5
S = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
K = [int(abs(math.sin(i + 1)) * (2**32)) & 0xFFFFFFFF for i in range(64)]

# Функція лівого повороту
def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

# Функція MD5
def md5(message):
    # Предпроцесування: додавання відступу до повідомлення
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    message += original_bit_len.to_bytes(8, byteorder='little')

    # Ініціалізація хешу:
    a0, b0, c0, d0 = 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476

    # Обробка повідомлення в частини 512 біт
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        M = [int.from_bytes(chunk[j:j+4], byteorder='little') for j in range(0, 64, 4)]

        A, B, C, D = a0, b0, c0, d0

        # Головний цикл MD5
        for j in range(64):
            if 0 <= j <= 15:
                F = (B & C) | (~B & D)
                g = j
            elif 16 <= j <= 31:
                F = (D & B) | (~D & C)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                F = B ^ C ^ D
                g = (3 * j + 5) % 16
            elif 48 <= j <= 63:
                F = C ^ (B | ~D)
                g = (7 * j) % 16

            F = (F + A + K[j] + M[g]) & 0xFFFFFFFF
            A, D, C, B = D, C, B, (B + left_rotate(F, S[j])) & 0xFFFFFFFF

        # Додаємо раніше отримані хеші цього фрагмента до отриманого результату:
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    # Отримуємо остаточне хеш-значення (big-endian) у вигляді 128-бітового числа:
    return b''.join(x.to_bytes(4, byteorder='little') for x in [a0, b0, c0, d0])

# Тестуємо MD5
def test_md5():
    # Тестові значення (взяті з RFC 1321: https://www.ietf.org/rfc/rfc1321.txt)
    test_cases = [
        (b"", "d41d8cd98f00b204e9800998ecf8427e"),
        (b"a", "0cc175b9c0f1b6a831c399e269772661"),
        (b"abc", "900150983cd24fb0d6963f7d28e17f72"),
        (b"message digest", "f96b697d7cb7938d525a2f31aaf161d0"),
        (b"abcdefghijklmnopqrstuvwxyz", "c3fcd3d76192e4007dfb496cca67e13b")
    ]
    for message, expected_hash in test_cases:
        result = md5(message).hex()
        print(f"MD5(\"{message.decode('utf-8')}\") = {result}")
        assert result == expected_hash
    print("Всі тести пройшли успішно!")

if __name__ == "__main__":
    test_md5()
