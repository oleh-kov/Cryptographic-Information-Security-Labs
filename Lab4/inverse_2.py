# Задвання №4

from phi import phi

def mod_exp(base, exp, mod):
    """
    Обчислює значення виразу base^exp по модулю mod.
    """
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def gcd(a, b):
    """
    Обчислює НСД a та b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    """
    Перевіряє, чи є задане число num простим.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def inverse_element_2(a, n):
    if gcd(a, n) != 1:
        raise ValueError("a i n не є взаємно простими, тому обернений елемент не існує.")
    
    def euler_theorem_inverse(a, n):
        # Обчислюємо функцію Ейлера phi(n) за допомогою імпортованої функції phi (з завдання №3)
        phi_n = phi(n)
        return mod_exp(a, phi_n - 1, n)
    
    def fermat_theorem_inverse(a, p):
        return mod_exp(a, p - 2, p)
    
    if is_prime(n):
        return fermat_theorem_inverse(a, n)
    else:
        return euler_theorem_inverse(a, n)

# Тестування на прикладі a=5 та n=18
a = 5
n = 18
print(f"Обернений елемент {a} за модулем {n} = {inverse_element_2(a, n)}")
