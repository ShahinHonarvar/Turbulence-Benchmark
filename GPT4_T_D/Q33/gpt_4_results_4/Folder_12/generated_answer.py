
def return_vowels(s):
    vowels = []
    for c in s[13:37]:
        if c > 'Z' and c <= '}' and c.lower() in 'aeiou':
            vowels.append(c)
    return vowels
