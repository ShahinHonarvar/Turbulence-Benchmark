
def return_vowels(str):
    str = str[50:77]
    vowels = "aeioru"
    result = [ch for ch in str if ch in vowels and ch > "#" and ch <= "r"]
    return result
