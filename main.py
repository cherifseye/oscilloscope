import sys
import oscilloscope
from PyQt5.QtWidgets import QApplication 


def main():
    app = QApplication(sys.argv)
    osc = oscilloscope.Oscilloscope()
    osc.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()