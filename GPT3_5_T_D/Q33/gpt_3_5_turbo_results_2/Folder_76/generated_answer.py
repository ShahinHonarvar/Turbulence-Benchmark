
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(495, 837):
        if string[index] in vowels and string[index] > 'B' and string[index] <= 't':
            result.append(string[index])
    return result
