import sys
List1 = ['1. Сумма всех цифр вещественного числа','2. task 2','3. task 3','4. task 4','5. task 5','6. Выход']
print('\n' * 100)

def enter_key_to_continue():
    input('================================================\nДля продолжения нажмите клавишу [ENTER]')
    main()

def error(x):
    print('\n' * 100)
    print(f'\n\n\nВНИМАНИЕ!!!\n    Вы ввели не существующую команду {x}... \n    Выберите команду из списка.')
    enter_key_to_continue()

# ========================= ДОМАШНЕЕ ЗАДАНИЕ ===========================

def Task01():
    num = float(input('Введите целое или вещественное число ->  '))
    n = num
    x = 1
    while x != 0:
        n = n*10
        x = n%1
    n = int(n)
    result = 0
    while n != 0:
        result = result + n%10
        n = n//10
    print(f'Сумма всех цифр числа {num} = {result}')

# def Task02():

# def Task03():

# def Task04():

# def Task05():

# ======================================================================

def choice(x):
    print(f'\n\n\n=================================================\n{List1[x-1]}')
    if x == 1:
        Task01()
    elif x == 2:
        print('Task 2')
    elif x == 3:
        print('Task 3')
    elif x == 4:
        print('Task 4')
    elif x == 5:
        print('Task 5')
    elif x == 6:
        sys.exit()
    enter_key_to_continue()

def main():
    Task = int(0)
    print('================================================\nВыберите действие...')
    print(*List1, sep='\n')
    Task = int(input('Введите номер операции ->  '))
    if 0 < Task <= len(List1):
        choice(Task)
    else:
        error(Task)

main()