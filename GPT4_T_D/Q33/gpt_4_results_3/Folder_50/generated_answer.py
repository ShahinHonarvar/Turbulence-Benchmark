
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    sub_str = s[11:53]
    return [i for i in sub_str if i in vowels and "+"' < i <= "W"]
