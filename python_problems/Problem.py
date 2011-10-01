class Problem:
    def __init__(self,intro,test):
        self.intro=intro
        self.test =test
    def __repr__(self):
        return "hello"
    def short_intro(self):
        return self.intro.split('\n')[0].replace('</a>','')
