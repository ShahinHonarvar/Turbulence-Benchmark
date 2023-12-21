
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for vowel in string[837:975]:
        if vowel in vowels and 'N' < vowel <= 'W':
            filtered_vowels.append(vowel)
    return filtered_vowels
