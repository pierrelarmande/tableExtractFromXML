class ArticleTable:
    caption = ''
    tableHead = []
    tableBody = []
    def __init__(self, filename):
        self.file = filename

    def setTableWrapFoot(self, tableWrapFoot):
        self.tableWrapFoot = tableWrapFoot

    def setTableCaption(self, caption=""):
        self.caption = caption


    def setTableHead(self,listThead):
        print(listThead)
        self.tableHead = listThead


    def setTableBody(self, listTbody):
        self.tableBody = listTbody
