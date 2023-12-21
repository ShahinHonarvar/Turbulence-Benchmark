
def return_vowels(s):
    vowel_list = 'aeiou'
    character_list = []
    for i in range(5,6):
        if s[i] in vowel_list and ord(s[i]) > ord('3') and ord(s[i])<= ord('^'):
            character_list.append(s[i])
    return character_list
