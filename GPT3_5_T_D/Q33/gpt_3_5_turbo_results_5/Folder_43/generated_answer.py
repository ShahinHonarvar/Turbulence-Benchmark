
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(22, 82):
        if string[i] in vowels and string[i] > 'N' and string[i] <= 'o':
            result.append(string[i])
    return result
