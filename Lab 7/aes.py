s_box = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

inv_sbox = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]



# Константи для розширення ключа
RCon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def sub_bytes(state):
    """Заміна байтів за допомогою S-боксу."""
    for i in range(4):
        for j in range(4):
            state[i][j] = s_box[state[i][j]]

def inv_sub_bytes(state):
    """Обмернена заміна байтів за допомогою S-боксу."""
    for i in range(4):
        for j in range(4):
            state[i][j] = inv_sbox[state[i][j]]

def shift_rows(state):
    """Зсув рядків матриці стану."""
    state[1][0], state[1][1], state[1][2], state[1][3] = state[1][1], state[1][2], state[1][3], state[1][0]
    state[2][0], state[2][1], state[2][2], state[2][3] = state[2][2], state[2][3], state[2][0], state[2][1]
    state[3][0], state[3][1], state[3][2], state[3][3] = state[3][3], state[3][0], state[3][1], state[3][2]

def inv_shift_rows(state):
    """Обернений зсув рядків матриці стану."""
    state[1] = state[1][-1:] + state[1][:-1]
    state[2] = state[2][-2:] + state[2][:-2]
    state[3] = state[3][-3:] + state[3][:-3]


MIX_COLUMNS_MATRIX = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

INV_MIX_COLUMNS_MATRIX = [
    [0x0E, 0x0B, 0x0D, 0x09],
    [0x09, 0x0E, 0x0B, 0x0D],
    [0x0D, 0x09, 0x0E, 0x0B],
    [0x0B, 0x0D, 0x09, 0x0E]
]

def mix_columns(state):
    """Змішування стовпців матриці стану."""
    for i in range(4):
        # Extract the column
        col = [state[j][i] for j in range(4)]
        #print(f"\ncol: {[hex(x) for x in col]}")
        # Perform the Mix Columns operation on the column
        new_col = [
            gmul(col[0], MIX_COLUMNS_MATRIX[0][0]) ^ gmul(col[1], MIX_COLUMNS_MATRIX[0][1]) ^ gmul(col[2], MIX_COLUMNS_MATRIX[0][2]) ^ gmul(col[3], MIX_COLUMNS_MATRIX[0][3]),
            gmul(col[0], MIX_COLUMNS_MATRIX[1][0]) ^ gmul(col[1], MIX_COLUMNS_MATRIX[1][1]) ^ gmul(col[2], MIX_COLUMNS_MATRIX[1][2]) ^ gmul(col[3], MIX_COLUMNS_MATRIX[1][3]),
            gmul(col[0], MIX_COLUMNS_MATRIX[2][0]) ^ gmul(col[1], MIX_COLUMNS_MATRIX[2][1]) ^ gmul(col[2], MIX_COLUMNS_MATRIX[2][2]) ^ gmul(col[3], MIX_COLUMNS_MATRIX[2][3]),
            gmul(col[0], MIX_COLUMNS_MATRIX[3][0]) ^ gmul(col[1], MIX_COLUMNS_MATRIX[3][1]) ^ gmul(col[2], MIX_COLUMNS_MATRIX[3][2]) ^ gmul(col[3], MIX_COLUMNS_MATRIX[3][3])
        ]
        # Place the new column back into the state
        for j in range(4):
            state[j][i] = new_col[j]
        #print(f"new_col = {[hex(x) for x in new_col]}")

def inv_mix_columns(state):
    """Обернене змішування стовпців матриці стану."""
    for i in range(4):
        # Extract the column
        col = [state[j][i] for j in range(4)]
        # Perform the Inverse Mix Columns operation on the column
        new_col = [
            gmul(col[0], INV_MIX_COLUMNS_MATRIX[0][0]) ^ gmul(col[1], INV_MIX_COLUMNS_MATRIX[0][1]) ^ gmul(col[2], INV_MIX_COLUMNS_MATRIX[0][2]) ^ gmul(col[3], INV_MIX_COLUMNS_MATRIX[0][3]),
            gmul(col[0], INV_MIX_COLUMNS_MATRIX[1][0]) ^ gmul(col[1], INV_MIX_COLUMNS_MATRIX[1][1]) ^ gmul(col[2], INV_MIX_COLUMNS_MATRIX[1][2]) ^ gmul(col[3], INV_MIX_COLUMNS_MATRIX[1][3]),
            gmul(col[0], INV_MIX_COLUMNS_MATRIX[2][0]) ^ gmul(col[1], INV_MIX_COLUMNS_MATRIX[2][1]) ^ gmul(col[2], INV_MIX_COLUMNS_MATRIX[2][2]) ^ gmul(col[3], INV_MIX_COLUMNS_MATRIX[2][3]),
            gmul(col[0], INV_MIX_COLUMNS_MATRIX[3][0]) ^ gmul(col[1], INV_MIX_COLUMNS_MATRIX[3][1]) ^ gmul(col[2], INV_MIX_COLUMNS_MATRIX[3][2]) ^ gmul(col[3], INV_MIX_COLUMNS_MATRIX[3][3])
        ]
        # Place the new column back into the state
        for j in range(4):
            state[j][i] = new_col[j]

def gmul(a, b):
    """Множення в галоевому полі."""
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xFF
        if high_bit_set:
            a ^= 0x1B
        b >>= 1
    return p

def add_round_key(state, round_key):
    """Додає раундовий ключ до стану."""
    print("Round Key:")
    for row in round_key:
        print([hex(x) for x in row])
    print("State before AddRoundKey:")
    for row in state:
        print([hex(x) for x in row])
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    print("State after AddRoundKey:")
    for row in state:
        print([hex(x) for x in row])

def key_expansion(key):
    """Розшиює 128-бітний ключ на раундові ключі."""
    expanded_keys = [list(key[i:i+4]) for i in range(0, len(key), 4)]
    for i in range(4, 44):
        temp = expanded_keys[i - 1]
        if i % 4 == 0:
            #print(f"Before Rotation and Substitution: {[hex(b) for b in temp]}")
            temp = [s_box[b] for b in temp[1:] + temp[:1]]
            #print(f"After Substitution: {[hex(b) for b in temp]}")
            temp[0] ^= RCon[i // 4 - 1]
            #print(f"After RCon XOR: {[hex(b) for b in temp]}")
        expanded_keys.append([expanded_keys[i - 4][j] ^ temp[j] for j in range(4)])
        #print(f"New Word: {[hex(b) for b in expanded_keys[-1]]}")
    return [expanded_keys[i:i+4] for i in range(0, len(expanded_keys), 4)]

def format_state_hex(state):
    """Форматує стан у шістнадцятковий рядок."""
    return '\n'.join(' '.join(f'{byte:02x}' for byte in row) for row in state)

def aes_encrypt_block(plaintext, key):
    """Зашифруємо блок AES-128."""
    state = [list(plaintext[i:i+4]) for i in range(0, len(plaintext), 4)]
    round_keys = key_expansion(key)
    print("Initial State:\n", format_state_hex(state))
    add_round_key(state, round_keys[0])
    print("After AddRoundKey (Round 0):\n", format_state_hex(state))
    for i in range(1, 10):
        #print(f"State before SubBytes (Round {i}):\n", format_state_hex(state))
        sub_bytes(state)
        print(f"After SubBytes (Round {i}):\n", format_state_hex(state))
        #print(f"State before ShiftRows (Round {i}):\n", format_state_hex(state))
        shift_rows(state)
        print(f"After ShiftRows (Round {i}):\n", format_state_hex(state))
        #print("State before MixColumns:\n", format_state_hex(state))
        mix_columns(state)
        print(f"After MixColumns (Round {i}):\n", format_state_hex(state))
        add_round_key(state, round_keys[i])
        print(f"After AddRoundKey (Round {i}):\n", format_state_hex(state))
    sub_bytes(state)
    print("After SubBytes (Round 10):\n", format_state_hex(state))
    print("State before ShiftRows (Round 10):\n", format_state_hex(state))
    shift_rows(state)
    print("After ShiftRows (Round 10):\n", format_state_hex(state))
    add_round_key(state, round_keys[10])
    print("After AddRoundKey (Round 10):\n", format_state_hex(state))
    return [byte for row in state for byte in row], round_keys

def aes_decrypt_block(ciphertext, key):
    """Розшифровуємо блок AES-128."""
    state = [list(ciphertext[i:i+4]) for i in range(0, len(ciphertext), 4)]
    round_keys = key_expansion(key)
    add_round_key(state, round_keys[10])
    for i in range(9, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, round_keys[i])
        inv_mix_columns(state)
    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, round_keys[0])
    return [byte for row in state for byte in row]

def format_expanded_key(round_keys):
    """З'єднює всі ключі раунду в один безперервний шістнадцятковий рядок. (розширений ключ як в CryptoTool)"""
    return ''.join(f'{byte:02x}' for key in round_keys for row in key for byte in row)

def format_hex_blocks(byte_list, block_size=8):
    """Форматує список байтів у безперервну шістнадцяткову строку, згруповану по блоках. (як в CryptoTool)"""
    hex_string = ''.join(f'{byte:02x}' for byte in byte_list)
    return ' '.join(hex_string[i:i + block_size] for i in range(0, len(hex_string), block_size))

def format_expanded_key_blocks(round_keys, block_size=8):
    expanded_hex = ''.join(f'{byte:02x}' for key in round_keys for row in key for byte in row)
    return ' '.join(expanded_hex[i:i + block_size] for i in range(0, len(expanded_hex), block_size))

# Example usage with formatted output

plaintext = [0x32, 0x88, 0x31, 0xe0,0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34]
key = [0x2b, 0x28, 0xab, 0x09, 0x7e, 0xae, 0xf7, 0xcf, 0x15, 0xd2, 0x15, 0x4f, 0x16, 0xa6, 0x88, 0x3c]


#plaintext = [0x00, 0x00, 0x01, 0x01, 0x03, 0x03, 0x07, 0x07, 0x0F, 0x0F, 0x1F, 0x1F, 0x3F, 0x3F, 0x7F, 0x7F]
#key = [0x00] * 16

# Encrypt and decrypt
ciphertext, round_keys = aes_encrypt_block(plaintext, key)
decrypted = aes_decrypt_block(ciphertext, key)

# Print in the required format
print("Вхідний текст:  ", format_hex_blocks(plaintext))
print("Стартовий ключ:  ", format_hex_blocks(key))
print("Розширений ключ:  ", format_expanded_key_blocks(round_keys))
print("Зашифрований текст:  ", format_hex_blocks(ciphertext))
print("Розшифрований текст:  ", format_hex_blocks(decrypted))