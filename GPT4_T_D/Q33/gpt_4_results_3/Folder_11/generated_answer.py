
def return_vowels(s):
    vowels_list = []
    vowels = 'aeiou'
    for char in s[29:73]:
        if char in vowels and '#' < char <= '(':
            vowels_list.append(char)
    return vowels_list
