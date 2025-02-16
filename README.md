## Description

Цей проєкт демонструє, як оцінити визначений інтеграл функції **f(x)=x\*\*2** на відрізку **[0, 1.856]** методом Монте-Карло. Результати порівнюються з аналітичним розв'язком та з результатом, отриманим за допомогою функції quad із бібліотеки SciPy.

## Input parameters:

- Функція: f(x)=x\*\*2
- Межі інтегрування: a=0, b=1.856
- Кількість випадкових точок: 10 000

## Results:

- Оцінка інтеграла методом Монте-Карло: 0.3293769899362066
- Аналітичне значення інтеграла : 0.3333333333333333
- Інтеграл: 0.33333333333333337 3.700743415417189e-15

## Conclusion

Як бачимо з отриманих результатів, оцінка інтеграла, знайдена за методом Монте-Карло (0.3293769899362066), досить близька до аналітичного значення
(0.33333333333333337). Різниця становить приблизно 0.004, що відповідає похибці близько 1%−2%. Це очікувана похибка для методу Монте-Карло з обмеженою кількістю випадкових точок, оскільки сам метод є статистичним і результат покращується зі збільшенням кількості випадкових вибірок.

Додатково, результат, отриманий за допомогою функції quad (0.0.3333333333333333), підтверджує правильність аналітичного розрахунку та свідчить про те, що наше наближення методом Монте-Карло є коректним. Таким чином, можна зробити висновок, що метод Монте-Карло добре справляється зі знаходженням площі під кривою навіть з відносно невеликою кількістю випадкових точок, а для зменшення відхилення від точного результату можна збільшувати обсяг вибірки.
