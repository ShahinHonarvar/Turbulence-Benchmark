
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(45, 76):
        if string[i] in vowels and string[i] > 'b' and string[i] <= 'z':
            result.append(string[i])
    return result
