
def return_vowels(str):
    vowels = 'aeiou'
    sub_str = str[149:313]
    vowel_list = [ch for ch in sub_str if ch in vowels and 'M' < ch <= 'j']
    return vowel_list
