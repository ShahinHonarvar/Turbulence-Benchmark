
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(495, 837):
        if string[index] in vowels and 'B' < string[index] <= 't':
            result.append(string[index])
    return result
