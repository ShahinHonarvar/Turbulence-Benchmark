
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[85:99]:
        if char in vowels and char > '/' and char <= 'n':
            result.append(char)
    return result
