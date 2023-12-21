
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    sublist = s[74:96]
    character_list = [c for c in sublist if c in vowels and c > "I" and c <= "X"]
    return character_list
