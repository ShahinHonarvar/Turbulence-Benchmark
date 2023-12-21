
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    
    for i in range(202, 872):
        char = string[i]
        if char in vowels and char > '3' and char <= '>':
            vowel_list.append(char)
    
    return vowel_list
