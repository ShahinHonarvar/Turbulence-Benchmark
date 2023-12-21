
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(46, 49):
        if string[i] in vowels and ord('[') < ord(string[i]) <= ord('p'):
            result.append(string[i])
    return result
