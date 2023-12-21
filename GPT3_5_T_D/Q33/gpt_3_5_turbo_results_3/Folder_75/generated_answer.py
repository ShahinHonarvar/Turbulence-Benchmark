
def return_vowels(string):
    vowels = "AEIOUaeiou"
    result = []
    for i in range(20, 41):
        if string[i] in vowels and string[i] > 'K' and string[i] <= 'Z':
            result.append(string[i])
    return result
