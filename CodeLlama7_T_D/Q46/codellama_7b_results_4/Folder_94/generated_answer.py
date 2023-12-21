 `def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 56, 88 and 51
    gcf = 1
    for i in range(56, 89, 2):
        if gcf > 1:
            break

        for j in range(88, 52, -2):
            if gcf > 1:
                break

            for k in range(51, 51, 0):
                if gcf > 1:
                    break

                common_factors = [i, j, k]
                for factor in common_factors:
                    if factor % gcf == 0:
                        continue

                    else:

                        break

                else:

                    gcf = max(common_factors)

    return gcf`
