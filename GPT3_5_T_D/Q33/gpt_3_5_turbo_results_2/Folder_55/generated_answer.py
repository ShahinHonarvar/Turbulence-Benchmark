
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(1, 5):
        if string[index] in vowels and '!' < string[index] <= 'j':
            result.append(string[index])
    return result
