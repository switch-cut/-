import sys

from PyQt5.QtWidgets import QApplication
from 数据库课程设计.ui import denluui


def main():
    app = QApplication(sys.argv)
    w = denluui.Ui_Form()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
