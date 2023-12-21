
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 38):
        if string[i].lower() in vowels and ord(string[i].lower()) > ord('n') and ord(string[i].lower()) <= ord('k'):
            result.append(string[i])
    return result
