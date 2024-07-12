print('Пространство имён')

calls = 0


def count_calls ():    # подсчитывающая вызовы остальных функций.
    global calls
    calls += 1


def string_info (string ):

    count_calls()  # ++ к-во вызовов

    return { len (string), string.upper(), string.lower()   }



def is_contains(string, list_to_search):

    count_calls() # ++ к-во вызовов

    cont = 0
    for str__ in list_to_search:
        if str__.upper() == string.upper(): # давим регистр, по ТЗ  UrbaN ~ URBAN.
            cont += 1
        #else:
             # do nothing
    if cont > 0: # Нашел минимум одно вхождение
        return True
    else:
        return False
        #return cont # ЛОгичнее возвращать к-во вхождений подстроки в список, но по ТЗ да/нет.




# void main(void) шутка. Маркер начала основной программы

print( string_info("Хара Мамбуру") )
print(is_contains ("Хара", ["Рамамба", "Хара", "Мамбуру"]))

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(f"Функции вызывались {calls} раз")

