
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if string[i].lower() in vowels and ord(string[i]) >= 5 and ord(string[i]) <= ord('m'):
            result.append(string[i])
    return result
