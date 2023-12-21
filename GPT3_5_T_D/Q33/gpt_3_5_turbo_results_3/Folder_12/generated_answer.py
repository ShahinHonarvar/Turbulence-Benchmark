
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for char in string[13:37]:
        if char in vowels and ord(char) > ord('Z') and ord(char) <= ord('}'):
            vowel_list.append(char)
    return vowel_list
