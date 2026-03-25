import matplotlib.pyplot as plt
import numpy as np

raw_data = {
    "Kuggo Kirin M5": [55, 60, 1000, 21, 35, 150],
    "Ninebot Max G30": [30, 65, 350, 15, 19.2, 100],
    "Xiaomi Mi Electric Scooter Pro 2": [25, 45, 300, 12.8, 14.2, 100],
    "Halten RS-02": [40, 50, 800, 18, 28, 130]
}

models = list(raw_data.keys())
char = list(raw_data.values())

name_char = [
    "Максимальная скорость(км/ч)",
    "Запас хода(км)",
    "Мощность мотора (Вт)",
    "Ёмкость батареи (А\Ч)",
    "Вес(кг)",
    "Максимальная нагрузка (кг)"
]

def get_normal(char):
    normal = []
    reverse_indices = [4]

    for item in char:
        normalized_item = []
        for idx, (a, b) in enumerate(zip(item, char[0])):
            if idx in reverse_indices:
                normalized_item.append(b / a if a != 0 else 0)
            else:
                normalized_item.append(a / b if b != 0 else 0)
        normal.append(normalized_item)
    return normal

def get_quality(normal):
    result = []
    for item in normal:
        result.append(round(sum(item) / len(item), 2))
    return result

def create_bar(name, values):
    plt.figure(figsize=(12, 6))
    plt.bar(name, values, color='skyblue')
    plt.xlabel("Модель", fontsize=12)
    plt.ylabel("Kту", fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.title("Коэффициент технического уровня (Kту)", fontsize=14)
    plt.subplots_adjust(bottom=0.35)
    plt.show()

def create_radial(models, name, values):
    values_copy = [item[:] for item in values]
    for item in values_copy:
        item.append(item[0])

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles.append(angles[0])

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(values_copy)):
        ax.plot(angles, values_copy[i], "o-", linewidth=2, label=models[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=10)

    max_val = max(max(item) for item in values_copy)
    ax.set_ylim(0, max_val * 1.1)

    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик", pad=20)
    plt.show()

normal = get_normal(char)
data = get_quality(normal)

create_bar(models, data)
create_radial(models, name_char, normal)