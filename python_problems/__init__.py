pset_list = ['mit-6.00-pset-1', 'mit-6.00-pset-2','golf','others']

def get_problems_in_pset(pset):
    if (pset == 'others'):
        from python_problems import problems
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
