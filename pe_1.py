def greatest_multiple_below(max_num: int, n: int) -> int:
    curr = max_num - 1
    while curr % n != 0:
        curr -= 1
    return curr


def sum_to_n(n: int) -> int:
    # Uses Gauss's Formula
    return 0.5 * n * (n + 1)


# Inclusion-Exclusion Principle
print(3 * sum_to_n(greatest_multiple_below(1000, 3) / 3) + 5 * sum_to_n(greatest_multiple_below(1000, 5) / 5) - 
        15 * sum_to_n(greatest_multiple_below(1000, 15) / 15))

