
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_range = []
    for char in string[70:76]:
        if char > string[2] and char <= ':':
            if char in vowels:
                vowels_range.append(char)
    return vowels_range
