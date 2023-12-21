
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(14, 60):
        if string[i].lower() in vowels and 'D' < string[i] <= 'v':
            result.append(string[i])
    return result
