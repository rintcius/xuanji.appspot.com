pset_list = ['others', 'golf', 'mit']

def get_problems_in_pset(pset):
    if (pset == 'others'):
        from python_problems import problems
        return problems
    if (pset == 'golf'):
        from golf import problems
        return problems
    if (pset == 'mit'):
        from mit import problems
        return problems
