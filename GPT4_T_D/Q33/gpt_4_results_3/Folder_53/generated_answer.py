
def return_vowels(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_range = s[27:57]
    vowels = []
    for char in s_range:
        if char in vowels_list and 'o' < char <= 'w':
            vowels.append(char)
    return vowels
