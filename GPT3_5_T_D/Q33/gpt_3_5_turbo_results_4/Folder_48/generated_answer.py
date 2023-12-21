
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(529, 828):
        if string[i] in vowels and string[i] > 'U' and string[i] <= 'l':
            result.append(string[i])
    return result
