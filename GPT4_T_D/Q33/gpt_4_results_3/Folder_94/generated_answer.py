
def return_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    specified_range = s[40:94]
    result_list = []
    for char in specified_range:
        if char in vowel_list and '4' < char <= 'H':
            result_list.append(char)
    return result_list
