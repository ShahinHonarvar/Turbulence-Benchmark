
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(10, 97):
        if string[i].lower() in vowels and string[i] > 'r':
            res.append(string[i])
    return res
