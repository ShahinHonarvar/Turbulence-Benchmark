
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(5, 6):
        if string[index] in vowels and string[3] < string[index] <= '^':
            result.append(string[index])
    return result
