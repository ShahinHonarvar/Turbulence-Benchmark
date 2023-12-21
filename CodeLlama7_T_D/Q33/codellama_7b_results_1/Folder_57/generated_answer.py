
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    index21 = 21 - 1
    index23 = 23 - 1
    result = []
    for i in range(index21, index23 + 1):
        if string[i].isalpha() and string[i].lower() in vowels:
            if string[i] > '-' and string[i] <= 'n':
                result.append(string[i])
    return result
