
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    index171 = string.find('I', 0) + 1
    index402 = string.find('k', 0)
    if index171 == -1 or index402 == -1:
        return []

    vowel_list = []

    for char in string[index171:index402]:

        if char in vowels and ord(char) > 73 and ord(char) <= 107:
            vowel_list.append(char)

    return vowel_list
