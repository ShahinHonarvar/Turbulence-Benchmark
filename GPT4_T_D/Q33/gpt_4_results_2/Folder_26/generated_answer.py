
def return_vowels(string):
    vowel_list = []
    string_part = string[10:82]
    for ch in string_part:
        if ch >= '$' and ch <= '@' and ch in 'aeiouAEIOU':
            vowel_list.append(ch)
    return vowel_list
