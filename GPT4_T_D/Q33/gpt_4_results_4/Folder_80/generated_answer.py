
def return_vowels(string):
    vowels = []
    for char in string[85:99]:
        if char in "aeiou" and "/" < char <= "n":
            vowels.append(char)
    return vowels
