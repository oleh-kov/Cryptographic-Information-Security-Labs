# Додав можливість роботи з двійковими і шістнадцятковими значеннями, як говорили на парі

def parse_input(value):
    """
    Парсить вхідне значення, яке може бути в шістнадцятковому або двійковому форматі.
    """
    if isinstance(value, str):
        value = value.strip()
        if value.startswith('0x'):
            return int(value, 16)  # Шістнадцятковий формат
        elif value.startswith('0b'):
            return int(value, 2)  # Двійковий формат
        else:
            raise ValueError("Непідтримуваний формат. Використовуйте 0x для шістнадцяткового або 0b для двійкового формату.")
    elif isinstance(value, int):
        return value  # Десятковий формат
    else:
        raise ValueError("Непідтримуваний формат. Введіть значення як рядок або ціле число.")

def mul02(byte):
    """
    Множення байту на 02 над полем Галуа GF(2^8)
    """
    byte = parse_input(byte)
    result = byte << 1  # Зсув вліво на 1 біт
    if byte & 0x80:  # Якщо старший біт був 1
        result ^= 0x1B  # Виконуємо XOR з 0x1B (m(x) без старшого біту)
    return result & 0xFF  # Повертаємо лише молодші 8 біт

def mul03(byte):
    """
    Множення байту на 03 над полем Галуа GF(2^8)
    """
    byte = parse_input(byte)
    return mul02(byte) ^ byte  # Використовуємо mul02 і виконуємо XOR з оригінальним байтом (Відповідно до зауваження №2)

if __name__ == "__main__":
    byte1 = '0xD4'  # 16-кове представлення байту
    byte2 = '0b10111111' # двійкове представлення байту | те саме, що і (0xBF) відповідно до таблиці

    result1 = mul02(byte1)
    result2 = mul03(byte2)

    print(f"D4 * 02 = {result1:02X}")
    print(f"0b10111111(0xBF) * 03 = {result2:02X}")