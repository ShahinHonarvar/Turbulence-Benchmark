
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    lst = [letter for letter in s[3:8] if letter in vowels and ';' < letter <= 'D']
    return lst
