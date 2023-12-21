
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if string[i] in vowels and 'B' < string[i] <= 'i':
            result.append(string[i])
    return result
