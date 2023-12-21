
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(46, 49):
        if string[i] in vowels and '[' < string[i] <= 'p':
            result.append(string[i])
    return result
