
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[32:61]:
        if char in vowels and '?' < char <= 'P':
            result.append(char)
    return result
