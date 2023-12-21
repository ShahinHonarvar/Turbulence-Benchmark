
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = [character for character in string[202:872] if character in vowels and '3' < character <= '>']
    return filtered_vowels
