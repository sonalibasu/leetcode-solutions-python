"""
Q: Assuming the letters are contiguous. Handling 2 edge cases of len 0 and 1
"""
def compress(s:str):
    if not s:
        return ''
    if len(s) == 1:
        return s+ '1'
    counter = 1
    compressed, current_char = '', s[0]
    for character in s[1:]:
        if character == current_char:
            counter += 1
        else:
            compressed = compressed + current_char + str(counter)
            current_char = character
            counter = 1
    compressed = compressed + current_char + str(counter)
    return compressed

print(compress('AAAAaaaaBBBFFFfffg'))

            
