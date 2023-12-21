
def return_vowels(s):
    vowels = 'aeiou'
    results = [char for char in s[17:65] if char.lower() in vowels and 'U' < char <= '{']
    return results
