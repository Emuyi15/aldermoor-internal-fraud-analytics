"""
Small statistical helpers used across the Aldermoor project
"""


def calculate_median(values: list[float]) -> float:

    """
        Return the median of a non-empty list of numbers

        Raises ValueError if values is empty. Does not modify the input.

    """
    if not values:
        raise ValueError(f"Cannot calculate the median of an empty list")

    sorted_values = sorted(values)
    n_values = len(sorted_values)
    middle = n_values // 2
    
    if n_values % 2 == 1:
        return sorted_values[middle]

    return (sorted_values[middle - 1] + sorted_values[middle]) / 2