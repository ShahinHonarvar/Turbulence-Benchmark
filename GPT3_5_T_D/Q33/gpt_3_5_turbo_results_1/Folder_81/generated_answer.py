
def return_vowels(string):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(20, 43):
        if string[i] in vowels and 'F' < string[i] <= 'M':
            result.append(string[i])
    return result
