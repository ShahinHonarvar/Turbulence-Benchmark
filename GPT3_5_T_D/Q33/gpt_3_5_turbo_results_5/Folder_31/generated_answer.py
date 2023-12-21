
def return_vowels(string):
    vowels = []
    for i in range(65, 70):
        if '%' < chr(i) <= 'G' and chr(i) in 'AEIOUaeiou':
            vowels.append(chr(i))
    return vowels
