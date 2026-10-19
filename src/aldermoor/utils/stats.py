"""
A function to calculate median from a given list and return float
"""

def calculate_median(values: list) -> float:

    '''
        calculate the median of any given list of numbers
        returns a float

        '''
    if not values:
        raise ValueError(f"Cannot calculate the median of an empty list")

    sorted_values = sorted(values)
    n_values = len(sorted_values)
    middle = n_values // 2
    
    if n_values % 2 == 1:
        return sorted_values[middle]

    return (sorted_values[middle - 1] + sorted_values[middle]) / 2