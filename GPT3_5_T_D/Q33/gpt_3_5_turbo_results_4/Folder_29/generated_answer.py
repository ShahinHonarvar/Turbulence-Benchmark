
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(19, 20):
        if string[i] > '<' and string[i] <= 'p' and string[i] in vowels:
            result.append(string[i])
    return result
