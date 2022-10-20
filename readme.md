# **Программа для расчёта рациональных или комплексных чисел с возможностью сохранения лога**
## **Архитектура программы:**
![Архитектура](pictures/Архитектура.jpg)

Программа работает по модульному принципу, где из одного модуля вытекает другой, а иногда происходит взаимодействие модулей для вывода информации пользователю на экран (модуль **UI.py**)
## **Описание работы программы:**
1. При запуске программы пользователю необходимо выбрать пункт меню, соответствующий его описанию:

![Основной_блок](pictures/main(controllerUI).jpg)

2. При выборе, например, вычисления рациональных чисел, пользователю необходимо ввести выражение, которое он желает вычислить:

![Рациональные_числа](pictures/rationalUI.jpg)
```
P.S.: При вводе неверных значений в любом из модулей программа выдаст предупреждение.
```
3. При выборе, например, вычисления комплексных чисел, пользователю необходимо ввести выражение, которое он желает вычислить:

![Комплексные_числа](pictures/complexUI.jpg)

4. Программа может выводить лог, в котором хранятся ранее вычисленные пользователем выражения:

![Лог](pictures/log.jpg)

```
P.S.: В случае с пустым журналом программа выдаст соответствующее предупреждение.
```
5. Также можно выйти из программы, введя 4 пункт меню:

![Выход](pictures/exit.jpg)

**Над приложением работал Кириллов Кирилл.**