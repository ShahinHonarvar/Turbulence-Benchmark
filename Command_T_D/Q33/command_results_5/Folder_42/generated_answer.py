def return_vowels(s):
    try:
        return [i for i in s[12:-1] if i.lower() in 'aeiou']
    except:
        pass
