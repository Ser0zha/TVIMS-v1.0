import matplotlib.pyplot as plt
import seaborn as sns


def plot_fern(xs, ys):
    plt.figure(figsize=(6, 10))
    plt.scatter(xs, ys, s=0.1, color='green')
    plt.title("Фрактал Барнсли")
    plt.axis('off')
    plt.show()


def plot_density(xs, ys):
    plt.figure(figsize=(6, 6))
    sns.kdeplot(x=xs, y=ys, cmap="Greens", fill=True, bw_adjust=0.1, levels=100, thresh=0.05)
    plt.title("Плотность распределения точек")
    plt.axis('equal')
    plt.show()
