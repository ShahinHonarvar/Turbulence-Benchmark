
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(45, 76):
        if string[i].lower() in vowels and 'b' < string[i].lower() <= 'z':
            result.append(string[i])
    return result
