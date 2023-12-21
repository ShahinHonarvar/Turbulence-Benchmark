import re
def all_pos_ints_exclusive(li):
    for i in range(18, 60):
        if str(i) in li:
            li.remove(str(i))
            break
    return li
