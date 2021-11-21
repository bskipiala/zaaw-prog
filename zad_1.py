def welcomeMessageFun(name: str, surname: str) -> str:
    welcomeMessage = (f'Cześć {name} {surname}!')
    return welcomeMessage

welcomeMessageFunResult = welcomeMessageFun('Jan', 'Kowalski')

print(welcomeMessageFunResult)