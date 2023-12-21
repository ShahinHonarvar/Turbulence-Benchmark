
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[31:37]:
        if char in vowels and char > ';' and char <= 't':
            result.append(char)
    return result
