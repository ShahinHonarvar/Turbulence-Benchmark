
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[19:20]:
        if char in vowels and char > '<' and char <= 'p':
            result.append(char)
    return result
