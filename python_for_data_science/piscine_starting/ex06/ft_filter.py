def ft_filter(fct, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which fct(item)
    is true. If function is None, return the items that are true.
    """
    if fct is None:
        return (item for item in iterable if item)
    return (item for item in iterable if fct(item))
