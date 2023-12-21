 def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    index202 = string.find('a', 202)
    if index202 == -1:
        return []

    index872 = string.find('a', 872)

    vowel_list = []

    for i in range(index202, index872 + 1):

        if string[i] in vowels and string[i] > '3' and string[i] <= '8':
            vowel_list.append(string[i])

    return vowel_list
