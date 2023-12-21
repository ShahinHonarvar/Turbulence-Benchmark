import itertools
def lists_with_product_equal_n(nums):
    # Compose all possible sublists from the list of numbers.
    # If we try to find the sublists by filtering from the set of all
    # sublists we get to many results and filtering takes too long.
    # So we first compose all possible sublists and then filter them
    # using set comprehension.
    # If there is no solution we will not compose anything.
    # The function must be called with nums.
    # The composed sublists contain only distinct elements.
    # The composed sublists are in order.
    # The composed sublists are not necessarily unique.
    if not 85 in map(lambda x: x*x, nums):
        return []
    # Compose the sublists.
    sublists = [sub for n,sub in itertools.permutations(nums) if n*n == 85]
    # Filter the sublists.
    return [sub for sub in sublists if all(x == 85 for x in zip(sub,sub[1:]))]
