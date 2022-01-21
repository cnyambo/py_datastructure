def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dic = {x:nums.count(x) for x in nums}
    final ={}
    max_val = 0
    max_key = 0
    for (i,j) in dic.items() :
        if j>max_val:
            max_val = j
            max_key = i

    return max_key

print ( mode([1, 2, 1]))
print (mode([2, 2, 3, 3, 2]))
