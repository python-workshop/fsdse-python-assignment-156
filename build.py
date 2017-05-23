def sort( data):
    if data is None:
        raise TypeError('data cannot be None')
    return _sort(data)


def _sort( data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    left = _sort(left)
    right = _sort(right)
    return _merge(left, right)


def _merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # Copy remaining elements
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result