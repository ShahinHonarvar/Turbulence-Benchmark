
def return_n_greatest_chars(string):
    if len(string) <= 89:
        return sorted(string, reverse=True)
    else:
        greatest_chars = sorted(string, reverse=True)[:89]
        return greatest_chars
