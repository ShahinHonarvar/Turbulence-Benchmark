
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(149, 313):
        if string[i].lower() in vowels and string[i] > 'm' and string[i] <= 'j':
            result.append(string[i])
    return result
