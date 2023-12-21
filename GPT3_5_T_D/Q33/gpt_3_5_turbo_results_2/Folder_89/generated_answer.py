
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[50:51]:
        if char > ',' and char <= 'v' and char.lower() in vowels:
            result.append(char)
    return result
