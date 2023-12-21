
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list_vowels = []
    for i in range(74, 96):
        if i < len(str) and str[i] in vowels and str[i] > 'i' and str[i] <= 'x':
            list_vowels.append(str[i])
    return list_vowels
