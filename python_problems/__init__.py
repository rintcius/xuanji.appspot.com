pset_list = {'a', 'b'}

def get_problems_in_pset(pset):
    if (pset == 'a'):
        from python_problems import problems
        return problems
    if (pset == 'b'):
        from more_problems import problems
        return problems
