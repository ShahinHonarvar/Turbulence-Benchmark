import re
def composite_nums_between_indices(lst):
    return set(i for i in range(639, 975) if re.fullmatch(r'(?!11)', str(i))) & set(lst)
