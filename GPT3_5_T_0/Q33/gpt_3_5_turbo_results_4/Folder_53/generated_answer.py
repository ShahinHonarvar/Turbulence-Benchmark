
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[27:57]:
        if char in vowels and 'o' < char <= 'w':
            result.append(char)
    return result
