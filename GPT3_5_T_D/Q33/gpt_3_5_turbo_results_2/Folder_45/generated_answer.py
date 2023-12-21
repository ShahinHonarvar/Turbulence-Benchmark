
def return_vowels(string):
    vowels = []
    for char in string[43:70]:
        if char > "*" and char <= "b" and char in "aeiouAEIOU":
            vowels.append(char)
    return vowels
