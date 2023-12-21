
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[74:96]:
        if char in vowels and 'I' < char <= 'X':
            result.append(char)
    return result
