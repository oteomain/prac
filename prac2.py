from numpy import linspace, log10, cos
from matplotlib.pyplot import subplots, show, savefig, tight_layout

def main():
    # Инициализация области построения
    x_vals = linspace(-4.5, 2, 400)
    
    # Вычисление значений функций
    lhs = log10(x_vals + 5)  # левая часть: lg(x+5)
    rhs = cos(x_vals)        # правая часть: cos(x)

    # Создание фигуры и осей
    fig, ax = subplots(figsize=(9, 5))

    # Построение кривых
    ax.plot(x_vals, lhs, label=r'$\lg(x+5)$', color='#FF8C00', linewidth=2.5, linestyle='-')
    ax.plot(x_vals, rhs, label=r'$\cos(x)$', color='#2E8B57', linewidth=2.5, linestyle='--')

    # Выделение интервала [-1, 0] полупрозрачной заливкой
    ax.axvspan(-1, 0, color='yellow', alpha=0.3, label='Интервал корня')

    # Настройка осей: перенос в центр координат
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Сетка
    ax.grid(True, linestyle=':', alpha=0.6)

    # Заголовок графика
    ax.set_title('Графический метод отделения корней: $\lg(x+5) = \cos(x)$', pad=15)

    # Ограничения отображения
    ax.set_xlim(-4.5, 2)
    ax.set_ylim(-1.5, 1.5)

    # Легенда
    ax.legend(loc='upper right', frameon=True, shadow=True)

    # Сохранение результата
    output_filename = 'root_localization_v2.png'
    tight_layout()
    savefig(output_filename, dpi=300)
    print(f"График сохранен в файл: {output_filename}")
    
    show()

if __name__ == "__main__":
    main()