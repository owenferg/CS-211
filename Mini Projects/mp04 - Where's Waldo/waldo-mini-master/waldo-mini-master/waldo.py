'''Owen Ferguson CS 211 2-7-24'''

Waldo = 'W'
Other = '.'

def all_row_exists_waldo(l):
    for row in l:
        if Waldo in row:
            return True
    return False

def all_col_exists_waldo(l):
    num_cols = len(l[0]) if l else 0
    for col in range(num_cols):
        for row in l:
            if row[col] == Waldo:
                return True
    return False


def all_row_all_waldo(l):
    for row in l:
        if not all(cell == Waldo for cell in row):
            return False
    return True

def all_col_all_waldo(l):
    num_cols = len(l[0]) if l else 0
    for col in range(num_cols):
        for row in l:
            if row[col] != Waldo:
                return False
    return True

def exists_row_all_waldo(l):
    for row in l:
        if all(cell == Waldo for cell in row):
            return True
    return False

def exists_col_all_waldo(l):
    num_cols = len(l[0]) if l else 0
    for col in range(num_cols):
        if all(row[col] == Waldo for row in l):
            return True
    return False

def exists_row_exists_waldo(l):
    for row in l:
        if Waldo in row:
            return True
    return False

def exists_col_exists_waldo(l):
    num_cols = len(l[0]) if l else 0
    for col in range(num_cols):
        for row in l:
            if row[col] == Waldo:
                return True
    return False
