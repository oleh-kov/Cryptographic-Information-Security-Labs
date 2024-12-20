# Еліптична крива Ель-Гамаля Шифрування

Цей код реалізує метод шифрування Ель-Гамаля з використанням еліптичних кривих.
Код призначений для шифрування та дешифрування повідомлення, представленого як точка на еліптичній кривій.

## Завдання

Зашифруйте повідомлення методом Ель-Гамаля, представивши його як точку \( P(66, 64) \) на еліптичній кривій, визначеній рівнянням \( y^2 = x^3 - x + 3 \) (mod 127), з базовою точкою (генератором) \( Q(66, 64) \). Завдання включає обчислення порядку базової точки, генерацію приватних та публічних ключів, шифрування повідомлення та його дешифрування.

## Алгоритм

1. **Параметри еліптичної кривої:**
   - Рівняння: \( y^2 = x^3 - x + 3 \) (mod 127)
   - Генераторна точка: \( G = (66, 64) \)

2. **Обчислення порядку точки:**
   - Використовуйте функцію `elliptic_curve_order` для визначення порядку генераторної точки.

3. **Генерація ключів:**
   - **Приватний ключ (d):** Випадково обраний цілий число.
   - **Публічний ключ (P):** Обчислюється як \( d \cdot G \) за допомогою скалярного множення.

4. **Шифрування:**
   - **Ефемерний ключ (k):** Випадково обраний цілий число.
   - **Шифротекст (C1, C2):**
     - \( C1 = k \cdot G \)
     - \( C2 = Pm + k \cdot P \)

5. **Дешифрування:**
   - Відновлення початкової точки повідомлення \( Pm \) за допомогою приватного ключа та шифротексту.

## Детальне пояснення коду

### Функції

- **`mod_inverse(a, p)`:**
  - Обчислює обернене по модулю число з використанням малої теореми Ферма.

- **`point_addition(P, Q, a, p)`:**
  - Додає дві точки на еліптичній кривій, обробляючи як подвоєння точки, так і додавання.

- **`scalar_multiplication(k, P, a, p)`:**
  - Множить точку на скаляр за допомогою методу подвоєння та додавання, виводячи кожен крок для наглядності.

- **`elliptic_curve_order(G, a, b, p)`:**
  - Визначає порядок точки на еліптичній кривій.

### Хід виконання коду

1. **Ініціалізація параметрів:**
   - Визначається еліптична крива та генераторна точка.

2. **Обчислення порядку:**
   - Обчислюється порядок генераторної точки.

3. **Генерація ключів:**
   - Генеруються приватні та публічні ключі.

4. **Шифрування повідомлення:**
   - Шифрується точка повідомлення та виведиться шифротекст.

5. **Дешифрування повідомлення:**
   - Розшифровується шифротекст та виводиться початкова точка повідомлення.

## Скріншот виконання програми

![image](https://github.com/user-attachments/assets/bad9cea2-dffd-4f88-94f4-3b5e838d0d6d)
