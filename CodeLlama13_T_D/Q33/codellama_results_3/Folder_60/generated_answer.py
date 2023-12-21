
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(24, 59):
        if string[i] in vowels and string[i] <= 'U':
            result.append(string[i])
    return result
