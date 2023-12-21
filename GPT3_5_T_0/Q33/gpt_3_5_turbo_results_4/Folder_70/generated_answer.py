
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(171, 402):
        if string[i] in vowels and 'I' < string[i] <= 'k':
            result.append(string[i])
    return result
