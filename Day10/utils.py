def flatten_and_sort(item):
    flat = []
    for x in item:
        if isinstance(x, list):
            flat.extend(x)
        else:
            flat.append(x)
    return sorted(flat)