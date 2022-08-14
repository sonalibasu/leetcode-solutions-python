def pair_sum(arr, k):
    # edge case where array has less than 2 elements.
    if len(arr) < 2:
        return 
    
    seen, output = set(), set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target),max(num,target)))

    return output

print(pair_sum([1,2,3,2,4,3],6))
