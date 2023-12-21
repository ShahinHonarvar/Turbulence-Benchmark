
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 68):
        if string[i].lower() in vowels and string[i] > 'm' and string[i] <= 'x':
            result.append(string[i])
    return result
