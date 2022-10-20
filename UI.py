from log import ReadData

def expRatio():
    return input("\nПожалуйста введите выражение с рациональными числами со скобками или без: ")

def expComplex():
    return input('\nПожалуйста введите выражение с комплексными числами формата "A ± Bj" со скобками или без: ')

def expError():
    print("\nПохоже, что-то в Вашем выражении неправильно...\nПожалуйста, поищите ошибку.")

def result(expressionStart, result):
    print(f"{expressionStart} = {result}")

def Greetings():
    print("""Добро пожаловать в калькулятор рациональных и комплексных чисел!
Выберите и введите соостветствующий пункт меню:

1. Расчёт рациональных чисел.
2. Расчёт комплексных чисел.
3. Вывод лога вычислений.
4. Выход из калькулятора.\n""")

def ByeBye():
    print("\nЧто ж, надеюсь, увидимся снова...")

def BadMenuChoice():
    print("Число введено неправильно.\nПожалуйста, попробуйте ещё раз.\n")

def LogOutMsg():
    print("\nИстория вычислений:\n")

def LogEmptyMsg():
    print("\nЛог пустой. Сначала выполните какое-нибудь вычисление.")

def PrintLog():
    array = ReadData()
    for i in range(len(array)): print(f"{i + 1}: {array[i]}")