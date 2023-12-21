
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:9]:
        if char in vowels and '?' < char <= 'k':
            result.append(char)
    return result
