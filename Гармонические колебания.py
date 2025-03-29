import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QSizePolicy)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class HarmonicOscillation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("График гармонического колебания")

        self.amplitude_label = QLabel("Амплитуда (м):")
        self.amplitude_input = QLineEdit()
        self.frequency_label = QLabel("Частота (Гц):")
        self.frequency_input = QLineEdit()
        self.phase_label = QLabel("Фаза (градусы):")
        self.phase_input = QLineEdit()
        self.plot_button = QPushButton("Построить")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.amplitude_label)
        input_layout.addWidget(self.amplitude_input)
        input_layout.addWidget(self.frequency_label)
        input_layout.addWidget(self.frequency_input)
        input_layout.addWidget(self.phase_label)
        input_layout.addWidget(self.phase_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

        self.plot_button.clicked.connect(self.plot_oscillation)

        self.plot_oscillation()


    def plot_oscillation(self):
        try:
            A = float(self.amplitude_input.text())
            f = float(self.frequency_input.text())
            phi_deg = float(self.phase_input.text())
        except ValueError:
            self.ax.clear()
            self.ax.text(0.5, 0.5, "Ошибка: Некорректные данные", ha='center', va='center', transform=self.ax.transAxes)
            self.canvas.draw()
            return

        phi_rad = np.radians(phi_deg)

        t = np.linspace(0, 5, 500)  

        x = A * np.sin(2 * np.pi * f * t + phi_rad)

        self.ax.clear() 
        self.ax.plot(t, x)
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Смещение (м)")
        self.ax.set_title("График гармонического колебания")
        self.ax.grid(True)  
        self.canvas.draw()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    oscillation = HarmonicOscillation()
    oscillation.show()
    sys.exit(app.exec_())
