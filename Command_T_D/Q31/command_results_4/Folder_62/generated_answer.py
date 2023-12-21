import re
def if_perfect_num(nums):
    str_list = list(map(str, nums))
    return bool(re.match(r"^(26|33|34|39|40|44|49|50|55|56|61|62|65|66|70|71|72|75|76|77|79|80|83|84|86|87|89|90|91|92|94|95|96|97|99)$", str_list[926]))
