
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    str = str[69:82]
    return [ch for ch in str if ch in vowels and ch > '[' and ch <= '~']
