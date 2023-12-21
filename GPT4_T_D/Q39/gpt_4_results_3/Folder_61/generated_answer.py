
def return_n_greatest_chars(s):
    sorted_string = sorted(list(s), reverse = True)
    if len(sorted_string) >=66:
        return sorted_string[:66]
    else:
        return "The given string does not have enough different characters"
