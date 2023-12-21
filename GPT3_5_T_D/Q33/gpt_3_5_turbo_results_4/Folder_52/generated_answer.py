
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[24:68]:
        if char > 'f' and char <= '|':
            if char.lower() in vowels:
                result.append(char)
    return result
