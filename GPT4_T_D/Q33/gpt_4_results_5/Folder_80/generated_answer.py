
def return_vowels(string):
    vowel_list = 'aeiou'
    res = [x for x in string[85:99] if x > '/' and x <= 'n' and x.lower() in vowel_list]
    return res
