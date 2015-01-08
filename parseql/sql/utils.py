"""
Shared utility functions
"""
from ..parsers import remove_comments
from ..parsers import remove_empty_statements
from ..parsers import split_statements
from ..parsers import remove_transactional
from ..parsers import remove_newlines


def atmost_one(*args):
    """Asserts one of the arguments is not None

    Returns:
        result(bool): True if exactly one of the arguments is not None
    """
    return sum([1 for a in args if a is not None]) <= 1


def sanatize_sql(sql, keep_transaction=False):
    """Sanatize the sql string
    """
    # remove comments
    string = remove_comments(sql)

    # remove transactionals
    if not keep_transaction:
        string = remove_transactional(string)

    # remove new lines
    string = remove_newlines(string)

    # remove empty statements
    string = remove_empty_statements(string)

    # split into multiple statements
    return split_statements(string)
