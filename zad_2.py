numbers = [1, 2, 3, 4, 5]
numbersMultiplied = []

def multiplyNumbers1(numbers):
    for number in numbers:
        number *= 2
        numbersMultiplied.append(number)
    return numbersMultiplied

def multiplyNumbers2(numbers):
    numbersMultiplied = [number * 2 for number in numbers]
    return numbersMultiplied