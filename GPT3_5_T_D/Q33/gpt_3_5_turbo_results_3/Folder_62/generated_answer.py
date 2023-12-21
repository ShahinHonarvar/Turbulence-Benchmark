
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(14, 60):
        if string[i] in vowels and ord(string[i]) > ord('D') and ord(string[i]) <= ord('v'):
            result.append(string[i])
    return result
