
def return_vowels(s):
    vowels = "AEIOUaeiou"
    lst = [i for i in s[202:872] if i in vowels and '3' < i <= '>']
    return lst
