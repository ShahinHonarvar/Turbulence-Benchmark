
def return_vowels(string):
    vowels = []
    for char in string[77:84]:
        if char in "aeiou" and char > "(" and char <= "G":
            vowels.append(char)
    return vowels
