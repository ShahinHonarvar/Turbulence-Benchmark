
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 51):
        if string[i] > ',' and string[i] <= 'v' and string[i].lower() in vowels:
            result.append(string[i])
    return result
