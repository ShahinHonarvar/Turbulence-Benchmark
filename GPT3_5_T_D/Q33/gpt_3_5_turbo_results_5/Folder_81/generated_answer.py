
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if i > 5 and string[i].lower() in vowels and string[i].lower() <= 'm':
            result.append(string[i])
    return result
