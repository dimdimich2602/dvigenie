import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class CoolingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моделирование охлаждения тела")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.label_t0 = QLabel("Начальная температура T0 (°C):")
        self.input_t0 = QLineEdit()
        self.layout.addWidget(self.label_t0)
        self.layout.addWidget(self.input_t0)
        
        self.label_tenv = QLabel("Температура окружающей среды Tenv (°C):")
        self.input_tenv = QLineEdit()
        self.layout.addWidget(self.label_tenv)
        self.layout.addWidget(self.input_tenv)
        
        self.label_k = QLabel("Коэффициент теплообмена k (1/с):")
        self.input_k = QLineEdit()
        self.layout.addWidget(self.label_k)
        self.layout.addWidget(self.input_k)

        self.button_plot = QPushButton("Построить")
        self.layout.addWidget(self.button_plot)
        self.button_plot.clicked.connect(self.plot_graph)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
    
    def plot_graph(self):
        try:
            T0 = float(self.input_t0.text())
            Tenv = float(self.input_tenv.text())
            k = float(self.input_k.text())

            if k <= 0:
                raise ValueError("Коэффициент теплообмена k должен быть больше 0.")

            t = np.linspace(0, 1000, 500)
            T = Tenv + (T0 - Tenv) * np.exp(-k * t)

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(t, T, label="Температура тела")
            ax.set_xlabel("Время (с)")
            ax.set_ylabel("Температура тела (°C)")
            ax.set_title("Охлаждение тела по закону Ньютона")
            ax.legend()
            
            self.canvas.draw()
        except ValueError as e:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.text(0.5, 0.5, str(e), fontsize=12, ha='center', va='center', transform=ax.transAxes)
            ax.axis("off")
            self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoolingApp()
    window.show()
    sys.exit(app.exec_())
