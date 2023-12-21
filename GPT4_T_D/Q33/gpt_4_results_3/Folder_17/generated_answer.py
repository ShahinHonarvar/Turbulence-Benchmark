
def return_vowels(s):
    vowels_list = []
    for i in range(60, min(len(s), 99)):
        if s[i] in 'aeiouAEIOU' and s[i] > 'j' and s[i] <= 'n':
            vowels_list.append(s[i])
    return vowels_list
