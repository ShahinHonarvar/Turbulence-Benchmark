
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(13, 37):
        if string[index] > 'Z' and string[index] <= '}':
            if string[index] in vowels:
                result.append(string[index])
    return result
