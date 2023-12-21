
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = string[86:99]
    final_vowels = []
    for char in subset:
        if char in vowels and ord('E') < ord(char) <= ord('r'):
            final_vowels.append(char)
    return final_vowels
