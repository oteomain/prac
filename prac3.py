from math import acos, log10, fabs

def solve_equation():
    # Функция итерационного процесса
    def get_next_x(x):
        return -acos(log10(x + 5))

    # Параметры расчета
    current_approx = -1.0   # Начальное приближение
    accuracy = 0.001        # Требуемая точность
    iteration = 0           # Счетчик шагов

    # Заголовок таблицы результатов
    print("Метод простых итераций")
    print(f"{'Итерация':<8} | {'x_n':<10} | {'x_n+1':<10} | {'|dx|':<10}")
    print("-" * 45)

    while True:
        # Вычисление следующего приближения
        next_approx = get_next_x(current_approx)
        
        # Оценка погрешности
        delta = fabs(next_approx - current_approx)
        
        # Вывод текущих данных
        print(f"{iteration:<8} | {current_approx:10.4f} | {next_approx:10.4f} | {delta:10.4f}")
        
        # Проверка условия остановки
        if delta <= accuracy:
            break
        
        # Подготовка к следующему шагу
        current_approx = next_approx
        iteration += 1

    print("-" * 45)
    print(f"Решение найдено: x ≈ {next_approx:.4f}")

def main():
    solve_equation()

if __name__ == "__main__":
    main()