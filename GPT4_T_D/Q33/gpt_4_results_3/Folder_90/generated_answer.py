
def return_vowels(a):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    range_str = a[142:145]
    return [c for c in range_str if c in vowels and '4' < c <= 'o']
