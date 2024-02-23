'''Owen Ferguson
Mini project: List Sweep Algorithms'''

def all_same(l: list) -> bool:
    '''Determines if all elements in a list are the same'''
    if l == []:
        return True

    matcher = l[0] # picks first item in list
    for item in l:
        if item != matcher:
            return False
    
    return True

def dedup(l: list) -> list:
    '''Returns a de-duplicated version of the input list'''
    if l == []:
        return []
    
    result = []
    current_value = l[0]

    for item in l:
        if item != current_value:
            result.append(current_value)
            current_value = item

    result.append(l[-1]) # loop doesnt get last item, this fixes
    return result

def max_run(l: list) -> int:
    '''Returns the longest "run", a subsequence with identical values'''
    if l == []:
        return 0

    longest_run = 0
    current_run = 0
    current_value = l[0] # first value compares with itself, which is why initially current_run = 0

    for item in l:
        if item == current_value:
            current_run += 1
            if current_run > longest_run:
                longest_run = current_run
        
        else:
            current_value = item
            current_run = 1 # subsequent values after first do not compare with themselves, so current_run = 1 accounting
    
    return longest_run