import clr
clr.AddReference('System.Data')
clr.AddReference('System.Windows.Forms')

from System.Data import DataTable
from System import Array
from System.Windows.Forms import DataGridView

class DatabaseTable:
    def __init__(self):
        self.createDataTable()
        self.dataGridView = DataGridView()
        self.dataGridView.Width = 360
        self.dataGridView.Height = 230
        self.dataGridView.DataSource = self.dataTable

    def createDataTable(self):
        self.dataTable = DataTable()
        self.dataTable.Columns.Add("", bool)
        self.dataTable.Columns.Add("Name", str)
        self.dataTable.Columns.Add("ID", str)
        self.dataTable.Rows.Add(Array[object]([True, "chatchawan", "Chatchawan ID"]))

    def getTable(self):
        return self.dataGridView
        