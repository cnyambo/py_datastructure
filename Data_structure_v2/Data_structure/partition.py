def is_even(num):
    return num % 2 == 0
def is_string(el):
    return isinstance(el, str)
def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    l1 = []
    l2 = []
    result =[]
    for i in lst:
        if fn ==is_even and is_even(i):
            l1.append(i)
        elif fn == is_string and is_string(i):
            l1.append(i)
        else:
            l2.append(i)
    result.append(l1)
    result.append(l2)
    
    return result

print (partition([1, 2, 3, 4], is_even))
print(partition(["hi", None, 6, "bye"], is_string))
