
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[11:53]:
        if char in vowels and char > '+' and char <= 'W':
            result.append(char)
    return result
