
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(20, 43):
        if string[index] in vowels and ord(string[index]) > ord('5') and ord(string[index]) <= ord('M'):
            result.append(string[index])
    return result
