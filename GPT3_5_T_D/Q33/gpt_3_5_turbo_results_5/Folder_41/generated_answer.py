
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[71:81]:
        if char in vowels and char > '>' and char <= 'U':
            result.append(char)
    return result
