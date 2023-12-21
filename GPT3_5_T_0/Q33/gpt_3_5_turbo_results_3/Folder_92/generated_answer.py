
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[3:8]:
        if char in vowels and char > ';' and char <= 'D':
            result.append(char)
    return result
