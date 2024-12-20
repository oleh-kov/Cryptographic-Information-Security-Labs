# README for elgamal_elyptic.py

## Завдання
Реалізувати асиметричний алгоритм шифрування (Ель-Гамаль на основі еліптичних кривих). Тестування для p=23, a=1, b=1 (крива \(y^2=(x^3+x^2+1) \mod 23\)), базова точка (генератор) - G = (17,20).

## Короткий опис алгоритму
Ель-Гамаль на еліптичних кривих використовує обчислення на еліптичних кривих для створення ключів, шифрування та дешифрування повідомлень. Використовує випадкові числа для генерації ключів та обчислення спільного секрету.

## Опис коду
- `EllipticCurve` клас: містить методи для додавання точок, скалярного множення, перевірки точок на кривій.
- `ElGamalECC` клас: реалізує генерацію ключів, шифрування та дешифрування.
- Функція `main()`: демонструє процес генерації ключів, шифрування та дешифрування з виведенням результатів на екран.

## Детальний опис
### Математичний контекст
Ель-Гамаль є асиметричним криптографічним алгоритмом, що забезпечує конфіденційність повідомлень за допомогою еліптичних кривих.

### Реалізація
- **Генерація ключів**: Кожен користувач генерує пару ключів (приватний та публічний) за допомогою скалярного множення базової точки.
- **Шифрування**: Повідомлення шифрується за допомогою публічного ключа отримувача та випадкового числа для обчислення спільного секрету.
- **Дешифрування**: Отримувач використовує свій приватний ключ для відновлення повідомлення з шифротексту, віднімаючи спільний секрет.

## Скріншот виконання програми

![image](https://github.com/user-attachments/assets/10ce2a0c-4fce-43df-b320-13693d643494)
