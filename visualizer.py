import matplotlib.pyplot as plt


class InteractiveFernPlot:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.fig, self.ax = plt.subplots(figsize=(6, 10))
        self.scatter = self.ax.scatter(xs, ys, s=0.1, color='green')
        self.ax.set_title("Интерактивный фрактал Барнсли")
        self.ax.axis('off')

        self.fig.canvas.mpl_connect('scroll_event', self.zoom)

    def zoom(self, event):
        base_scale = 1.2
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()

        xdata = event.xdata
        ydata = event.ydata
        if xdata is None or ydata is None:
            return

        if event.button == 'up':
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            scale_factor = base_scale
        else:
            scale_factor = 1

        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

        relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
        rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

        self.ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * relx])
        self.ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * rely])
        self.fig.canvas.draw_idle()


def plot_interactive_fern(xs, ys):
    InteractiveFernPlot(xs, ys)
    plt.show()
