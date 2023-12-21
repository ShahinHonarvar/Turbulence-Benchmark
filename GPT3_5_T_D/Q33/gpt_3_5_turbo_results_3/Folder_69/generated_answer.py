
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(641, 872):
        if string[i] in vowels and '>' < string[i] <= 'q':
            result.append(string[i])
    return result
