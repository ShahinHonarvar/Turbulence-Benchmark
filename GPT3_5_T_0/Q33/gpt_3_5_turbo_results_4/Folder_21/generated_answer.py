
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(464, 574):
        if string[i] in vowels and 'a' < string[i] <= 'g':
            result.append(string[i])
    return result
