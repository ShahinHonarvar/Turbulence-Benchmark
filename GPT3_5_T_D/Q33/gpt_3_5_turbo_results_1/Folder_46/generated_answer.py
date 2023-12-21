
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 83):
        if string[i] in vowels and '%' < string[i] <= 'e':
            result.append(string[i])
    return result
