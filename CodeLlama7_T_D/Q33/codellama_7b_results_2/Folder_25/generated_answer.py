
def return_vowels(string):
    vowels = []
    for char in string[28:76]:
        if char.isalpha() and char.lower() in "aeiou":
            vowels.append(char)
    return vowels
