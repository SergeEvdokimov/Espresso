import io
import sys
import sqlite3
import PyQt5.uic as uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QAbstractScrollArea

con = sqlite3.connect("coffee.sqlite")
cur = con.cursor()

ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>15</x>
      <y>21</y>
      <width>771</width>
      <height>521</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class CoffeeHouse(QMainWindow):
    def __init__(self):
        super().__init__()

        temp = io.StringIO(ui)
        uic.loadUi(temp, self)
        self.setWindowTitle('Кофейня')
        self.show_data()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

    def show_data(self):
        query = cur.execute(f'''select * from coffee''').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(query))
        title = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                 'Описание вкуса', 'Цена,\nруб', 'Объем упаковки,\nмл']
        self.tableWidget.setHorizontalHeaderLabels(title)

        for i, elem in enumerate(query):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeHouse()
    window.show()
    sys.exit(app.exec())