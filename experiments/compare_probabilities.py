from generator import generate_barnsley_fern
from visualizer import plot_fern
from analyzer import compute_statistics

EXPERIMENTS = [
    ([0.01, 0.85, 0.07, 0.07], "Стандартные вероятности"),
    ([0.05, 0.75, 0.10, 0.10], "Изменённые вероятности #1"),
    ([0.10, 0.65, 0.15, 0.10], "Изменённые вероятности #2"),
]

for probs, label in EXPERIMENTS:
    print(f"\n--- {label} ---")
    xs, ys = generate_barnsley_fern(probs=probs)
    plot_fern(xs, ys)
    stats = compute_statistics(xs, ys)
    print(f"Математическое ожидание x: {stats['mean_x']:.4f}")
    print(f"Математическое ожидание y: {stats['mean_y']:.4f}")
    print(f"Дисперсия x: {stats['var_x']:.4f}")
    print(f"Дисперсия y: {stats['var_y']:.4f}")
    print(f"Корреляция между x и y: {stats['correlation']:.4f}")