
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    sub_str = s[10:82]
    return [x for x in sub_str if x in vowels and '$' < x <= '@']
