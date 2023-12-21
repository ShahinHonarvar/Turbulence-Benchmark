
def return_vowels(str):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    sub_str = str[37:57]
    return [char for char in sub_str if char in vowels and "*" < char <= "P"]
