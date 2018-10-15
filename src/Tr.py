# This class wil manage all td tags under the tr's tags
"""
    <tr>
        <td> data1 <td>
        <td> data2 <td>
    </tr>
"""

class Tr:
    listOTd = []
    def __init__(self, listTd=None):
        self.listOfTd = listTd


    # add a td to the list of tds
    def addTdToListOfTd(self, td):
        pass