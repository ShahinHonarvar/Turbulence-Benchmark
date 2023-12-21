
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(604, 949):
        if string[index] in vowels and 'N' < string[index] <= 'U':
            result.append(string[index])
    return result
