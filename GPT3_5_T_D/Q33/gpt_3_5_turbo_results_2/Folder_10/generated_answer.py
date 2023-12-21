
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(31, 37):
        if string[i] in vowels and ord(string[i]) > ord(';') and ord(string[i]) <= ord('t'):
            vowel_list.append(string[i])
    return vowel_list
