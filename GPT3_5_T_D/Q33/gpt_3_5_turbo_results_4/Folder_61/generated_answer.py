
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:4]:
        if char in vowels and 'C' < char <= 'I':
            result.append(char)
    return result
