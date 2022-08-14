def check(s:str):
    tracker = []
    for character in s:
        if character in tracker:
            return False
        else:
            tracker.append(character)
    return True

def check2(s:str):
    if len(set(s)) != len(s):
        return False
    return True

print(check2('AAA'))