
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(837, 975):
        if string[i] in vowels and 'N' < string[i] <= 'W':
            result.append(string[i])
    return result
