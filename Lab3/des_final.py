# Початкова перестановка
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]     

# Зворотня початкова перестановка
IP_inv = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25] 

# Розширення
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]  

# Перестановка P
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]  

# Перестановка вибору 1      
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4] 

# Перестановка вибору 2
PC_2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32] 

# S-бокси (8 блоків)    
S_BOX = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]    

def str_to_bin(user_input):
    """
    Перетворює рядок на двійкове представлення, впевнючись, що воно 64 біти довжиною.
    """
    binary_representation = ''.join(format(ord(char), '08b') for char in user_input)[:64]
    return binary_representation.ljust(64, '0')

def binary_to_ascii(binary_str):
    """
    Перетворює двійкове представлення на ASCII.
    """
    return ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))

def ip_on_binary_rep(binary_representation):
    """
    Застосовує початкову перестановку на двійкове представлення.
    """
    ip_result = [binary_representation[IP[i] - 1] for i in range(64)]
    return ''.join(ip_result)

def key_in_binary_conv():
    """
    Перетворює заданий ключ на двійкове представлення.
    """
    original_key = 'abcdefgh'
    return ''.join(format(ord(char), '08b') for char in original_key)

def generate_round_keys():
    """
    Генерує 16 раундових ключів для алгоритму DES.
    """
    binary_representation_key = key_in_binary_conv()
    pc1_key_str = ''.join(binary_representation_key[bit - 1] for bit in PC_1)

    c0, d0 = pc1_key_str[:28], pc1_key_str[28:]
    round_keys = []

    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    for round_num in range(16):
        c0 = c0[shift_schedule[round_num]:] + c0[:shift_schedule[round_num]]
        d0 = d0[shift_schedule[round_num]:] + d0[:shift_schedule[round_num]]
        cd_concatenated = c0 + d0
        round_key = ''.join(cd_concatenated[bit - 1] for bit in PC_2)
        round_keys.append(round_key)

    return round_keys

def encryption(user_input):
    """
    Шифрує вхідний текст за допомогою алгоритму DES.
    """
    binary_rep = str_to_bin(user_input)
    round_keys = generate_round_keys()
    ip_result_str = ip_on_binary_rep(binary_rep)
    lpt, rpt = ip_result_str[:32], ip_result_str[32:]

    for round_num in range(16):
        # Розширюємо 32-бітову праву половину до 48 біт
        expanded_result = ''.join(rpt[i - 1] for i in E)
        # Виконуємо операцію XOR з раундовим ключем
        xor_result_str = ''.join(str(int(expanded_result[i]) ^ int(round_keys[round_num][i])) for i in range(48))

        # Виконуємо підстановку за допомогою S-боксів
        s_box_substituted = ''
        for i in range(8):
            row_bits, col_bits = int(xor_result_str[i * 6] + xor_result_str[(i + 1) * 6 - 1], 2), int(xor_result_str[i * 6 + 1: (i + 1) * 6 - 1], 2)
            # Шукаємо значення S-боксу
            s_box_substituted += format(S_BOX[i][row_bits][col_bits], '04b')

        # Виконуємо перестановку P
        p_box_result = ''.join(s_box_substituted[i - 1] for i in P)
        # Виконуємо операцію XOR з лівою половинкою
        new_rpt = ''.join(str(int(lpt[i]) ^ int(p_box_result[i])) for i in range(32))

        # Мінємо ліву та праву половинки
        lpt, rpt = rpt, new_rpt

    # Виконуємо остаточну перестановку
    final_result = rpt + lpt
    final_cipher = ''.join(final_result[IP_inv[i] - 1] for i in range(64))
    final_cipher_ascii = binary_to_ascii(final_cipher)

    return final_cipher, final_cipher_ascii

def decryption(final_cipher):
    """
    Розшифровує остаточний шифр за допомогою алгоритму DES.

    Алгоритм розшифровки DES працює подібно до алгоритму шифрування, але з наступними відмінностями:

    1. Раундові ключі застосовуються у зворотньому порядку (тобто 16-й раундовий ключ застосовується перший, потім 15-й раундовий ключ, тощо.).
    2. Операція обміну виконується після підстановки за допомогою S-боксів, а не перед нею.

    """
    round_keys = generate_round_keys()[::-1]
    ip_dec_result_str = ip_on_binary_rep(final_cipher)
    lpt, rpt = ip_dec_result_str[:32], ip_dec_result_str[32:]

    for round_num in range(16):
        # Розширюємо 32-бітову праву половину до 48 біт
        expanded_result = ''.join(rpt[i - 1] for i in E)
        
        # Виконуємо операцію XOR з раундовим ключем
        xor_result_str = ''.join(str(int(expanded_result[i]) ^ int(round_keys[round_num][i])) for i in range(48))

        # Виконуємо підстановку за допомогою S-боксів
        s_box_substituted = ''
        for i in range(8):
            row_bits, col_bits = int(xor_result_str[i * 6] + xor_result_str[(i + 1) * 6 - 1], 2), int(xor_result_str[i * 6 + 1: (i + 1) * 6 - 1], 2)
            # Шукаємо значення S-боксу
            s_box_substituted += format(S_BOX[i][row_bits][col_bits], '04b')

        # Виконуємо перестановку P
        p_box_result = ''.join(s_box_substituted[i - 1] for i in P)

        # Виконуємо операцію XOR з лівою половинкою
        new_rpt = ''.join(str(int(lpt[i]) ^ int(p_box_result[i])) for i in range(32))

        # Мінємо ліву та праву половинки
        lpt, rpt = rpt, new_rpt

    # Виконуємо остаточну перестановку
    final_result = rpt + lpt
    final_cipher = ''.join(final_result[IP_inv[i] - 1] for i in range(64))
    final_cipher_ascii = binary_to_ascii(final_cipher)

    return final_cipher_ascii

# Тестування програми
if __name__ == "__main__":
    user_input = input("Введіть рядок: ")

    # Шифрування
    final_cipher, final_cipher_ascii = encryption(user_input)
    print("Шифрований текст:", final_cipher)

    # Розшифровка
    enc_to_binary = str_to_bin(final_cipher_ascii)
    dec = decryption(enc_to_binary)
    print("Розшифрований текст:", dec)
