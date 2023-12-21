
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in string[23:57]:
        if i > string[0] and i <= 'd' and i in vowels:
            result.append(i)
    return result
