
def return_vowels(string):
    vowels = []
    for char in string[65:70]:
        if char.isalpha() and char > '%' and char <= 'G' and char.lower() in ('a', 'e', 'i', 'o', 'u'):
            vowels.append(char)
    return vowels
