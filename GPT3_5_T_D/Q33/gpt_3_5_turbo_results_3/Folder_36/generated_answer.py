
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(604, 949):
        if string[i].lower() in vowels and 'n' < string[i].lower() <= 'u':
            result.append(string[i])
    return result
