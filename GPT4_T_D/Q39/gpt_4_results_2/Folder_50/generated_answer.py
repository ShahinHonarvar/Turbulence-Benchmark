
def return_n_greatest_chars(string):
    if len(string) >= 16:
        return sorted(string, key=ord, reverse=True)[:16]
    else:
        return 'The string should have at least 16 distinct characters'
