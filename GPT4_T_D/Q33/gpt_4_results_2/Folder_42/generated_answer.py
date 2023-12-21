
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = []
    for char in s[12:39]:
        if char in vowels and ';' < char <= '|':
            filtered_vowels.append(char)
    return filtered_vowels
