
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    results = []
    for i in range(11, 61):
        char = string[i]
        if char in vowels and 'M' < char <= 'W':
            results.append(char)
    return results
