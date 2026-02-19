from math import log10, cos, sin, log, fabs

def func(x):
    # Вычисление значения функции
    return log10(x + 5) - cos(x)

def deriv(x):
    # Вычисление производной функции
    return 1 / ((x + 5) * log(10)) + sin(x)

def solve_numerical_methods():
    # Параметры расчета
    accuracy = 0.001
    
    # Метод Хорд
    print("Метод хорд")
    print(f"{'Итерация':<8} | {'x_n':<10} | {'x_n+1':<10} | {'|dx|':<10}")
    print("-" * 45)

    fixed_point = -1.0
    val_fixed = func(fixed_point)
    
    current_approx = 0.0
    iteration = 0

    while True:
        val_current = func(current_approx)
        next_approx = current_approx - (val_current * (current_approx - fixed_point)) / (val_current - val_fixed)
        
        delta = fabs(next_approx - current_approx)
        
        print(f"{iteration:<8} | {current_approx:10.4f} | {next_approx:10.4f} | {delta:10.4f}")
        
        if delta <= accuracy:
            break
        
        current_approx = next_approx
        iteration += 1

    print("-" * 45)
    print(f"Решение (хорды): x ≈ {next_approx:.4f}\n")

    # Метод Ньютона
    print("Метод Ньютона")
    print(f"{'Итерация':<8} | {'x_n':<10} | {'x_n+1':<10} | {'|dx|':<10}")
    print("-" * 45)

    current_approx = -1.0
    iteration = 0

    while True:
        val_current = func(current_approx)
        deriv_current = deriv(current_approx)
        
        next_approx = current_approx - val_current / deriv_current
        
        delta = fabs(next_approx - current_approx)
        
        print(f"{iteration:<8} | {current_approx:10.4f} | {next_approx:10.4f} | {delta:10.4f}")
        
        if delta <= accuracy:
            break
        
        current_approx = next_approx
        iteration += 1

    print("-" * 45)
    print(f"Решение (Ньютон): x ≈ {next_approx:.4f}")

def main():
    solve_numerical_methods()

if __name__ == "__main__":
    main()