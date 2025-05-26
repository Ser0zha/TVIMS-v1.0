from generator import generate_barnsley_fern
from visualizer import plot_fern, plot_density
from analyzer import compute_statistics

if __name__ == "__main__":
    xs, ys = generate_barnsley_fern()
    plot_fern(xs, ys)
    plot_density(xs, ys)
    stats = compute_statistics(xs, ys)

    # print("\n--- Статистические характеристики ---")
    # print(f"Математическое ожидание x: {stats['mean_x']:.4f}")
    # print(f"Математическое ожидание y: {stats['mean_y']:.4f}")
    # print(f"Дисперсия x: {stats['var_x']:.4f}")
    # print(f"Дисперсия y: {stats['var_y']:.4f}")
    # print(f"Корреляция между x и y: {stats['correlation']:.4f}")
