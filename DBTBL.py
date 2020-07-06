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
        self.dataGridView.AllowUserToAddRows = False
        self.dataGridView.DataSource = self.dataTable

        self.dataGridView.CellClick += self.cellPressed

    def createDataTable(self):
        self.dataTable = DataTable()
        self.dataTable.Columns.Add(" ", bool)
        self.dataTable.Columns.Add("Name", str)
        self.dataTable.Columns.Add("ID", str)
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))
        self.dataTable.Rows.Add(Array[object]([False, "chatchawan", "Chatchawan ID"]))


    def cellPressed(self, sender, args):
        if(args.ColumnIndex == 0):
            if(bool(self.dataGridView.Rows[args.RowIndex].Cells[0]) == True):
                print("True")
            else :
                print("False")

    def getTable(self):
        return self.dataGridView
        