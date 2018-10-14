# This class will manage all the tr tags under the tbody's tage
"""
    <tbody>
        <tr>
            <td> data1 <td>
            <td> data2 <td>
        </tr>
        <tr>
            <td> data3 <td>
            <td> data4 <td>
        </tr>
    </tbody>
"""

class Tbody:
    def __init__(self, listTr):
        self.listOfTr = listTr