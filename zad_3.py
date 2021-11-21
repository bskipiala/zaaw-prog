def isEven(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

checkEven = isEven(2)

if checkEven == True:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')