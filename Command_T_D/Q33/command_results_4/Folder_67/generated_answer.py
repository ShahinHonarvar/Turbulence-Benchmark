def return_vowels(str1):
    str1 = str1[21:59]
    if len(str1) == 0:
        return []
    str1 = str1.split('/')
    str1 = str1[1:]
    str1 = str1.split('a')
    return [x for x in str1 if x in 'AEIOU']
