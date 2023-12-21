
def return_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_s = s[328:455]
    vowel_s = [char for char in sub_s if char in vowel_list and char > '<' and char <= 'z']
    return vowel_s
