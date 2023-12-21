
def return_n_smallest_chars(string):
    if len(string) <= 70:
        return sorted(string, key=lambda c: ord(c), reverse=True)
    else:
        return sorted(string, key=lambda c: ord(c), reverse=True)[:70]
