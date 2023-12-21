
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_s = s[328:455]
    vowels_list = [c for c in sub_s if c in vowels and ord('<')<ord(c)<=ord('z')]
    return vowels_list
