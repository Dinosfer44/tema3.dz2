while True:
    user_input = input("Введите любое число: ")
    try:
        chislo = int(user_input)
        print (f"Результат: {chislo}")
        break
    except ValueError:
        print ("Ошибка: введенное значение не является числом. Попробуйте еще раз.")

