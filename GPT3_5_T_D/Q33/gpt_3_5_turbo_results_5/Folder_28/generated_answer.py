
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(41, 50):
        if string[i] in vowels and 'W' < string[i] <= '[':
            result.append(string[i])
    return result
