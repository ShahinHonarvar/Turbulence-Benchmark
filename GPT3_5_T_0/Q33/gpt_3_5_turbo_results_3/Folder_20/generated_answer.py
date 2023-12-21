
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[59:61]:
        if char in vowels and char > '+' and char <= 'h':
            result.append(char)
    return result
