
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(2, 7):
        if string[index] > '^' and string[index] <= 'd' and string[index] in vowels:
            result.append(string[index])
    return result
