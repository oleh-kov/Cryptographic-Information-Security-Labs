# Завдання №2

from evklid import gcdex

def inverse_element(a, n):
    gcd, x, _ = gcdex(a, n)
    if gcd == 1:
        return x % n
    else:
        return None  # Обернений елемент не існує, якщо НСД не дорівнює 1

a, n = 5, 18
inverse = inverse_element(a, n)
print(f"Мультиплікативний обернений елемент числа {a} за модулем {n} = {inverse}")