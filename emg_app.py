import sys
from random import randint

#  1. import QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui


def lotto_generator() -> str:
    """Generate lotto numbers and lucky stars for euro millions draw"""

    lotto_numbers = set()
    lucky_stars = set()

    while len(lotto_numbers) != 5:  # Loop until set count is five
        lotto_numbers.add(randint(1, 50))  # add number to the list
    lotto_numbers = str(sorted(lotto_numbers)).strip("[]")  # Sort numbers and strip brackets

    while len(lucky_stars) != 2:
        lucky_stars.add(randint(1, 12))
    lucky_stars = str(sorted(lucky_stars)).strip("[]")

    return "Your Euro Millions Lottery numbers are:" \
           "\n\n  Lotto numbers: {0} \n\n  Lucky stars: {1} \n\nGood luck!".format(lotto_numbers, lucky_stars)


#  2. Create an instance of QApplication
app = QApplication(sys.argv)

#  3. Create an instance of your applications GUI
window = QWidget()
window.setWindowIcon(QtGui.QIcon('emimage.jpg'))
window.setWindowTitle("Euro Millions Generator")
window.setGeometry(100, 100, 360, 180)
window.move(300, 300)
helloMsg = QLabel(str(lotto_generator()), parent=window)
helloMsg.setFont(QtGui.QFont("Arial", 14))
helloMsg.move(20, 10)

#  4. Show the applications GUI
window.show()

#  5. Run application main loop
sys.exit(app.exec_())
