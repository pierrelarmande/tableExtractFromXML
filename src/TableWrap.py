# Table class

class TableWrap:
    listTable = []
    listOfTableHead = []
    listOfTableData = []
    def __init__(self, id, orientation=None, position=None):
        self.tableWrapAttribute = {
                                    'id':id,
                                    'orientation':orientation,
                                    'position':position
                                  }

    def setObjectIdValue(self, objectvalue=None):
        self.objectIdValue = objectvalue

    def setLabel(self, label=None):
        self.label = label

    def setCaption(self, caption=None):
        self.caption = caption

    def setAlternative(self, alternative=None):
        self.alternative = alternative

    def setOrientation(self, orientation=None):
        self.orientation = orientation

    def setTable(self, table):
        self.listTable.append(table)

    def setListTableHearder(self, listHeaderName):
        self.listOfTableHead.append(listHeaderName)