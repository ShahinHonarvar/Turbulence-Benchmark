
def return_vowels(string):
    vowels = []
    for char in string[20:43]:
        if 'A' <= char <= 'M' and char not in ['E', 'I', 'O', 'U']:
            vowels.append(char)
    return vowels
