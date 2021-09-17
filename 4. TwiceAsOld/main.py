def is_bigger(son, dad):
    if son < dad:
        return True
    else:
        return False


def twice_as_old(dad_years_old, son_years_old):
    if is_bigger(son_years_old, dad_years_old):
        son_years_old = son_years_old * 2
        return abs(dad_years_old - son_years_old)
