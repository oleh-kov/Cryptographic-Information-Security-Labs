import random

def miller_rabin(p, k):
    if p <= 3 or p % 2 == 0:
        return "Вхідні дані некоректні. p має бути > 3 і непарним."
    
    # Знаходимо s і d
    s, d = 0, p - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    
    # Виконуємо k раундів
    for _ in range(k):
        a = random.randint(2, p - 2)
        x = pow(a, d, p)
        
        if x == 1 or x == p - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        else:
            return f"Складене число"
    
    probability = 1 - (1/4)**k
    return f"Ймовірно просте число з ймовірністю {probability:.4f}"

# Приклад використання
if __name__ == "__main__":
    prime_number = 631  # Число для перевірки (просте)
    composite_number = 561  # Число для перевірки (складне)

    print(f"Число {prime_number}: {miller_rabin(prime_number, 5)}")
    print(f"Число {composite_number}: {miller_rabin(composite_number, 5)}")