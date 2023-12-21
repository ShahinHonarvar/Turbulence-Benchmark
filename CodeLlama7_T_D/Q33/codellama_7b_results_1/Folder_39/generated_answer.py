
def return_vowels(string):
    vowels = []
    for i in range(32, 97):
        char = string[i]
        if char.isalpha() and char.lower() in "aeiou" and char > "Q":
            vowels.append(char)
    return vowels
