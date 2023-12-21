
def return_vowels(s):
    vowels_list = []
    vowels = "aeiou"
    for char in s[34:69]:
        if char in vowels and char > '_' and char <= 'o':
            vowels_list.append(char)
    return vowels_list 
