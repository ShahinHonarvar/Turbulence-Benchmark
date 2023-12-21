
def find_original_set(*sets):
    result_set = set()
    for subset in sets:
        result_set |= subset
    return result_set
