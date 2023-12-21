
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    vowels_in_range = []
    for char in s[65:70]:
        if char > '%' and char <= 'G' and char in vowels:
            vowels_in_range.append(char)
    return vowels_in_range
