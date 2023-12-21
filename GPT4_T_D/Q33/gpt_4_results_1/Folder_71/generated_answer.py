
def return_vowels(string):
    vowels = 'aeiou'
    result = [ch for ch in string[36:56] if ch > '+' and ch <= '/' and ch.lower() in vowels]
    return result
