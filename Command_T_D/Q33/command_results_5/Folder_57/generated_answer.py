def return_vowels(str):
    str = str.split('')
    for i in range(21,23):
        if str[i] in 'AEIOUAEIOU':
            yield str[i]
