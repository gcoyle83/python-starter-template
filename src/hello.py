# var=1
# var=var


def toyou(x):
    return f"hi {x}"


def add(x):
    return x + 1


def subtract(x):
    return x - 1


def bad_formatting():
    """
    This is a poorly formatted function
    """
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    return x + y


def good_formatting():
    """
    This one's well formatted so shouldn't trigger an autocommit
    """
    return 2 + 2
