"""
Text standardization helpers for aldermoor category values (roles, systems, actions). 
"""


def standardize_text(value: str) -> str:
    '''
        Standardise a messy category value to lowercase snake_case.
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