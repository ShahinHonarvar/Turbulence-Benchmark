
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for letter in string[50:51]:
        if letter > ',' and letter <= 'v' and letter.lower() in vowels:
            vowels_in_range.append(letter)
    return vowels_in_range
