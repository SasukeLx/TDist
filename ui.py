import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeView, QFileSystemModel

class XMLViewer(QMainWindow):
   def __init__(self):
       super().__init__()

       self.setWindowTitle("TestCase Manager")

       self.model = QFileSystemModel()
       self.model.setRootPath("")

       self.tree = QTreeView()
       self.tree.setModel(self.model)
       self.tree.setRootIndex(self.model.index(""))

       self.setCentralWidget(self.tree)

       self.setMinimumSize(600, 400)

#    def open_file(self):
#        options = QFileDialog.Options()
#        options |= QFileDialog.ReadOnly
#        file_name, _ = QFileDialog.getOpenFileName(self, "Open XML File", "", "XML Files (*.xml);;All Files (*)", options=options)
#        if file_name:
#            self.model.setRootPath(file_name)
#            self.tree.setRootIndex(self.model.index(file_name))

#    def save_file(self):
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        file_name, _ = QFileDialog.getSaveFileName(self, "Save XML File", "", "XML Files (*.xml);;All Files (*)", options=options)
#        if file_name:
#            with open(file_name, "w") as f:
#                for index in range(self.tree.model().rowCount()):
#                    item = self.tree.model().item(index)
#                    f.write(f"{item.text()}\n")

if __name__ == "__main__":
   app = QApplication(sys.argv)

   window = XMLViewer()
   window.show()

   sys.exit(app.exec_())