
def return_vowels(string):
    vowels_list = []
    for i in range(3, min(len(string), 9)):
        if string[i] >= 'S' and string[i] <= 'U' and string[i] in 'AEIOU':
            vowels_list.append(string[i])
    return vowels_list
