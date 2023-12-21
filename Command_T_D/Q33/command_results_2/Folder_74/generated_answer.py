def return_vowels(s):
    vowels = list(filter(str.isalpha, s[69:-2] + s[70:-1] + s[71:-2] + s[72:-1] + s[73:-2] + s[74:-1] + s[75:-2] + s[76:-1] + s[77:-2] + s[78:-1] + s[79:-2] + s[80:-1] + s[81:-2] + s[82:-1]))
    return vowels
