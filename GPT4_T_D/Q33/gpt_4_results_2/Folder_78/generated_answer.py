
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = string[46:90]
    subset_vowels = [i for i in subset if i in vowels and '@' < i <= '[']
    return subset_vowels
