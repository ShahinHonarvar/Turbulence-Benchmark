
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(44, 95):
        if string[i] > string[5] and string[i] <= '<':
            if string[i] in vowels:
                result.append(string[i])
    return result
