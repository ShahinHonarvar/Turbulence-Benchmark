
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[43:70]:
        if char in vowels and char > '*' and char <= 'b':
            result.append(char)
    return result
