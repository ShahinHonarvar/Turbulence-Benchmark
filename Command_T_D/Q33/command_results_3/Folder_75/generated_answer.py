def return_vowels(str1):
    str1 = str1[20:]
    str1 = str1[:41]
    str1 = str1.split('')
    str1 = [i for i in str1 if i in 'AEIOU']
    return str1
