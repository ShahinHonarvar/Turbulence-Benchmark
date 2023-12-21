
def return_vowels(string):
    vowels = []
    for char in string[47:89]:
        if char.isalpha() and char.lower() in "aeiou":
            vowels.append(char)
    return vowels
