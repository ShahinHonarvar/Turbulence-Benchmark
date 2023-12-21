
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(837, 975):
        if string[i].lower() in vowels:
            result.append(string[i])
    return result
