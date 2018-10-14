# This class is used to manage the table tag
"""
<table>
    <thead>
        <tr>
            <td> data1 <td>
            <td> data2 <td>
        </tr>
        <tr>
            <td> data3 <td>
            <td> data4 <td>
        </tr>
    </thead>
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
</table>
"""
class Table:
    def __init__(self, thead, tbody):
        self.thead = thead
        self.tbody = tbody