
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []

    for char in string[69:82]:
        if char in vowels and '[' < char <= '~':
            result.append(char)
    
    return result
