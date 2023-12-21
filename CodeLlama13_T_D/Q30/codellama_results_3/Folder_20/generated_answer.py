
def insert_before_character(string):
    return "".join([f"H{c}" if c == 'C' else c for c in string])
