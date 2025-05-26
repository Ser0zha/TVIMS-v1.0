import matplotlib.pyplot as plt
import numpy as np


class BarnsleyFern:
    def __init__(self, n_points=100000):
        self.n_points = n_points
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.x, self.y = self.generate_fern()
        self.setup_plot()

    def generate_fern(self):
        x = np.zeros(self.n_points)
        y = np.zeros(self.n_points)

        for i in range(1, self.n_points):
            r = np.random.random()
            if r < 0.01:
                x[i] = 0
                y[i] = 0.16 * y[i - 1]
            elif r < 0.86:
                x[i] = 0.85 * x[i - 1] + 0.04 * y[i - 1]
                y[i] = -0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6
            elif r < 0.93:
                x[i] = 0.2 * x[i - 1] - 0.26 * y[i - 1]
                y[i] = 0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6
            else:
                x[i] = -0.15 * x[i - 1] + 0.28 * y[i - 1]
                y[i] = 0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44

        return x, y

    def setup_plot(self):
        self.ax.scatter(self.x, self.y, s=0.1, color='green', marker='.')
        self.ax.set_title('Barnsley Fern Fractal')
        self.ax.axis('off')

        # Подключаем обработчики событий
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.current_zoom = 1.0

    def on_click(self, event):
        if event.inaxes != self.ax:
            return

        if event.button == 1:  # Левая кнопка мыши - приближение
            self.zoom(event.xdata, event.ydata, 2.0)
        elif event.button == 3:  # Правая кнопка мыши - отдаление
            self.zoom(event.xdata, event.ydata, 0.5)

    def on_scroll(self, event):
        if event.inaxes != self.ax:
            return

        # Масштабирование колесиком мыши
        zoom_factor = 1.1 if event.step > 0 else 0.9
        self.zoom(event.xdata, event.ydata, zoom_factor)

    def zoom(self, x, y, factor):
        self.current_zoom *= factor

        # Получаем текущие границы
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        # Вычисляем новые границы
        new_width = (xlim[1] - xlim[0]) / factor
        new_height = (ylim[1] - ylim[0]) / factor

        self.ax.set_xlim([x - new_width / 2, x + new_width / 2])
        self.ax.set_ylim([y - new_height / 2, y + new_height / 2])

        self.fig.canvas.draw()


if __name__ == "__main__":
    fern = BarnsleyFern()
    plt.tight_layout()
    plt.show()
