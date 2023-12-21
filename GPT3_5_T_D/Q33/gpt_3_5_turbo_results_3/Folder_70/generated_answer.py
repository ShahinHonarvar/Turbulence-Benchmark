
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(171, 402):
        if string[index] in vowels and ord(string[index]) > ord('i') and ord(string[index]) <= ord('k'):
            result.append(string[index])
    return result
