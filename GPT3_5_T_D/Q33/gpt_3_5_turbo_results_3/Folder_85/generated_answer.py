
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(55, 65):
        if string[i] > 'Z' and string[i] <= 'w' and string[i].lower() in vowels:
            result.append(string[i])
    return result
