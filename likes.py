def likes(names: list) -> str:
    if not names:
        return ('no one likes this')
    if len(names) == 1:
        return (f'{names[0]} likes this')
    if len(names) == 2:
        return (f'{names[0]} and {names[1]} like this')
