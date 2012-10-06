pset_list = ['misc', 'mit-6.00-pset-1', 'mit-6.00-pset-2','golf','sicp','ucb']

def get_problems_in_pset(pset):
    if (pset == 'misc'):
        from others import problems
        return problems
    if (pset == 'golf'):
        from golf import problems
        return problems
    if (pset == 'mit-6.00-pset-1'):
        from mit import problems_1
        return problems_1
    if (pset == 'mit-6.00-pset-2'):
        from mit import problems_2
        return problems_2
    if (pset == 'sicp'):
        from sicp import problems
        return problems
    if (pset == 'ucb'):
        from ucb import problems
        return problems
