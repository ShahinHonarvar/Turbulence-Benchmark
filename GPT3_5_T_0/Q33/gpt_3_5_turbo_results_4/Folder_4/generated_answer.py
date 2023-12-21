
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[40:91]:
        if char.lower() in vowels and 'A' < char <= 'x':
            result.append(char)
    return result
