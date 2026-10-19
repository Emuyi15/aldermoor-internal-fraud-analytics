"""
A function to standardize all set of categorical
"""
def standardize_text(value: str) -> str:
    '''
        Cleans up messy categorical values

        Handles whitespace, runs of spaces, newlines,
        hyphens and repeated underscores.
    '''
    clean_value = "_".join(
        value.lower()
        .replace("-", " ")
        .replace("_", " ")
        .split()
    )

    return clean_value