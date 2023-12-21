
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for char in string[59:61]:
        if char > '+' and char <= 'h' and char in vowels:
            vowels_in_range.append(char)
    return vowels_in_range
