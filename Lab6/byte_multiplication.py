from galua import mul02  # Імпортуємо функцію mul02 з файлу galua.py

# Функція для перетворення числа в шістнадцятковий формат вручну
def to_hex(value):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while value > 0:
        result = hex_digits[value % 16] + result
        value //= 16
    return result if result else "0"

# Функція для множення поліномів
def multiply_polynomials(p1, p2):
    result = p2
    results = [p2]
    coefficients = get_polynomial_coefficients(p1)
    print("\nstep 0:", bits_to_polynomial(result), "\n-")

    for i in range(1, coefficients[0] + 1):
        previous_result = result
        result = mul02(result)  # Використовуємо mul02 з galua.py
        
        # Додатковий вивід у двійковому форматі
        binary_prev_result = f"{bin(previous_result)[2:]:>8}"
        binary_result = f"{bin(result)[2:]:>8}"
        binary_output = f"({binary_prev_result}) XOR ({binary_result}) = {binary_result}\n-"
        
        print(f"step {i}: {bits_to_polynomial(result)} {binary_output}")

        results.append(result)

    final_result = 0
    for idx in coefficients:
        final_result ^= results[idx]

    return final_result

# Функція для отримання коефіцієнтів полінома
def get_polynomial_coefficients(binary):
    coefficients = []
    for i in range(7, -1, -1):
        if binary & (1 << i):
            coefficients.append(i)
    return coefficients

# Функція для перетворення бітів у поліном
def bits_to_polynomial(bits):
    polynomial = []
    for i in range(7, -1, -1):
        if bits & (1 << i):
            if i == 0:
                polynomial.append("1")
            else:
                polynomial.append(f"x^{i}")
    return " + ".join(polynomial)

# Тестування
p1 = 0x57  # 0b01010111 | x^6 + x^4 + x^2 + x + 1
p2 = 0x83  # 0b10000011 | x^7 + x + 1

result = multiply_polynomials(p1, p2)
print("Result:", to_hex(result))