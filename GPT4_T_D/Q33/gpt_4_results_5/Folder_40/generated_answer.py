
def return_vowels(s):
    vowels_lst = []
    for char in s[2:7]:
        if char in 'aeiouAEIOU' and '^' < char <= 'd':
            vowels_lst.append(char)
    return vowels_lst
