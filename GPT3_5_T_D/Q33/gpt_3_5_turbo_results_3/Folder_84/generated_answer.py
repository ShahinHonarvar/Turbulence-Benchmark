
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if string[i].lower() in vowels and string[i].lower() > 'b' and string[i].lower() <= 'i':
            result.append(string[i])
    return result
