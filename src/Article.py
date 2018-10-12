# artcle

class Article:
    # contains a list of table-wrap of the article
    listTableWrap = []
    listTableAlternatives = []
    def __init__(self, title):
        self.title = title

    def setListOfTableWrap(self, tableWrap):
        self.listTableWrap.append(tableWrap)

    def setListOfTableWrapAlternatives(self,tableWrapAlternatives):
        self.listTableAlternatives.append(tableWrapAlternatives)