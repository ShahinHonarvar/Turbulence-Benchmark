
def return_vowels(s):
    vowel_list = []
    for i in range(1, 5):
        if s[i] in 'aeiou' and '!' < s[i] <= 'j':
            vowel_list.append(s[i])
    return vowel_list
