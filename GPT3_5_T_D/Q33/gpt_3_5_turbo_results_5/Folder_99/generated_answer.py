
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(323, 526):
        if string[index] in vowels and '+' < string[index] <= ':':
            result.append(string[index])
    return result
