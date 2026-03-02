import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd

def zavdannia_a():
    print("=" * 60)
    print("ЗАВДАННЯ А) Побудова графіків y(x) = x^(n/x)")
    print("=" * 60)

    systems = [2, 8, 10, 16]
    x = np.linspace(0.5, 5, 1000)

    plt.figure()
    for n in systems:
        y = x ** (n / x)
        plt.plot(x, y, label=f"n = {n}")

    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("y(x) = x^(n/x)")
    plt.legend()
    plt.grid()
    plt.show()


def zavdannia_b():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ Б) Доведення співвідношення")
    print("=" * 60)

    print("\nВИХІДНЕ РІВНЯННЯ:")
    print("dy/dx = n·x⁻²·(1 − ln(x))·y")

    print("\nРОЗДІЛЕННЯ ЗМІННИХ:")
    print("dy / y = n·x⁻²·(1 − ln(x)) dx")

    print("\nІНТЕГРУВАННЯ:")
    print("∫ dy / y = ∫ n·x⁻²·(1 − ln(x)) dx")

    print("\nРЕЗУЛЬТАТ:")
    print("ln y = (n ln x) / x + C")

    print("\nРОЗВ'ЯЗОК:")
    print("y(x) = C · x^(n/x)")

    print("\n" + "=" * 60)
    print("ЧИСЛОВА ПЕРЕВІРКА")
    print("=" * 60)

    def diff_eq(y, x, n):
        return y * (n / x**2) * (1 - np.log(x))

    x_range = np.linspace(0.5, 5, 1000)
    y0 = 1.0
    systems = [2, 8, 10, 16]

    for n in systems:
        y_sol = odeint(diff_eq, y0, x_range, args=(n,))
        print(f"\nn = {n}")
        print("-" * 40)
        for x_val in [1, 2, 3, 4]:
            idx = np.argmin(np.abs(x_range - x_val))
            print(f"y({x_val}) ≈ {y_sol[idx][0]:.6f}")

    n_test = 2
    x_test = 2.0
    y_sol_test = odeint(diff_eq, y0, x_range, args=(n_test,))
    idx_test = np.argmin(np.abs(x_range - x_test))
    y_test = y_sol_test[idx_test][0]

    dy_dx_numeric = (
        y_sol_test[idx_test + 1][0] - y_sol_test[idx_test - 1][0]
    ) / (
        x_range[idx_test + 1] - x_range[idx_test - 1]
    )

    right_side = y_test * (n_test / x_test**2) * (1 - np.log(x_test))

    print("\nПЕРЕВІРКА В ТОЧЦІ x = 2:")
    print(f"dy/dx (числ.) ≈ {dy_dx_numeric:.6f}")
    print(f"Права частина ≈ {right_side:.6f}")
    print(f"Різниця ≈ {abs(dy_dx_numeric - right_side):.8f}")


def zavdannia_9():
    print("\n" + "=" * 60)
    print("ЗАВДАННЯ 9) Інформація та ентропія")
    print("=" * 60)

    frequencies = {
        'SPACE': 0.134, 'о': 0.082, 'н': 0.070, 'а': 0.070,
        'и': 0.056, 'т': 0.051, 'в': 0.046, 'е': 0.043,
        'р': 0.038, 'і': 0.037, 'с': 0.036, 'к': 0.036,
        'м': 0.033, 'л': 0.028, 'д': 0.028, 'у': 0.027,
        'п': 0.025, 'я': 0.021, 'з': 0.019, 'ь': 0.015,
        'г': 0.013, 'ч': 0.011, 'б': 0.010, 'х': 0.010,
        'ц': 0.009, 'ю': 0.009, 'ж': 0.008, 'й': 0.007,
        'ф': 0.005, 'ш': 0.005, 'щ': 0.003
    }

    total = sum(frequencies.values())
    frequencies = {k: v / total for k, v in frequencies.items()}

    print("\n" + "─" * 60)
    print("ЧАСТИНА 1: Аналіз 32 окремих символів")
    print("─" * 60)

    df = pd.DataFrame(
        [(k, p, -np.log2(p)) for k, p in frequencies.items()],
        columns=["Символ", "p", "I (біт)"]
    ).sort_values(by="p", ascending=False)

    print("\nТаблиця частот для 32 символів:")
    print(df.to_string(index=False))

    n = 32
    H_max = np.log2(n)
    H_real = sum(-p * np.log2(p) for p in frequencies.values())

    print("\nЕнтропія (32 символи):")
    print(f"  H_max = log₂(32) = {H_max:.6f} біт/символ")
    print(f"  H = -Σ pᵢ·log₂(pᵢ) = {H_real:.6f} біт/символ")
    print(f"  Надмірність = {(1 - H_real / H_max) * 100:.2f}%")

    print("\n" + "─" * 60)
    print("ЧАСТИНА 2: Аналіз 2 класів символів (голосні/інші)")
    print("─" * 60)

    vowels = {'а', 'е', 'и', 'і', 'о', 'у', 'я', 'ю', 'є'}

    p_vowels = sum(p for k, p in frequencies.items() if k.lower() in vowels)
    p_other = 1 - p_vowels

    binary_data = [
        ("Голосні", p_vowels, -np.log2(p_vowels)),
        ("Інші", p_other, -np.log2(p_other))
    ]

    df_binary = pd.DataFrame(
        binary_data,
        columns=["Символ", "p", "I (біт)"]
    ).sort_values(by="p", ascending=False)

    print("\nТаблиця частот для 2 класів символів:")
    print(df_binary.to_string(index=False))

    H_bin_max = np.log2(2)
    H_bin = -p_vowels * np.log2(p_vowels) - p_other * np.log2(p_other)

    print("\nЕнтропія (2 символи):")
    print(f"  H_max = log₂(2) = {H_bin_max:.6f} біт/символ")
    print(f"  H = -Σ pᵢ·log₂(pᵢ) = {H_bin:.6f} біт/символ")
    print(f"  Надмірність = {(1 - H_bin / H_bin_max) * 100:.2f}%")

    print("\n" + "─" * 60)
    print("ДЕТАЛІЗАЦІЯ 2 КЛАСІВ:")
    print("─" * 60)
    
    # Показуємо які літери входять до кожного класу
    vowel_list = sorted([k for k in frequencies.keys() if k.lower() in vowels])
    other_list = sorted([k for k in frequencies.keys() if k.lower() not in vowels])
    
    print(f"\nГолосні ({len(vowel_list)} символів):")
    print(f"  {', '.join(vowel_list)}")
    print(f"  Сумарна ймовірність: {p_vowels:.4f}")
    
    print(f"\nІнші символи ({len(other_list)} символів):")
    print(f"  {', '.join(other_list[:10])}...")  # Показуємо перші 10
    print(f"  Сумарна ймовірність: {p_other:.4f}")

    return frequencies, H_max, H_real, H_bin_max, H_bin


def main():

    zavdannia_a()
    zavdannia_b()
    frequencies, H_max_32, H_real_32, H_max_2, H_real_2 = zavdannia_9()

    print("\n" + "=" * 60)
    print("ПІДСУМОК")
    print("=" * 60)
    
    print("\n32 ОКРЕМИХ СИМВОЛИ:")
    print(f"  H_max = {H_max_32:.4f} біт")
    print(f"  H = {H_real_32:.4f} біт")
    print(f"  Надмірність = {(1 - H_real_32 / H_max_32) * 100:.2f}%")
    
    print("\n2 КЛАСИ СИМВОЛІВ (ГОЛОСНІ/ІНШІ):")
    print(f"  H_max = {H_max_2:.4f} біт")
    print(f"  H = {H_real_2:.4f} біт")
    print(f"  Надмірність = {(1 - H_real_2 / H_max_2) * 100:.2f}%")
    
    print("\nПОРІВНЯННЯ:")
    print(f"  Різниця в ентропії: {H_real_32 - H_real_2:.4f} біт")
    print(f"  Втрата інформації при групуванні: {(1 - H_real_2/H_real_32)*100:.2f}%")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()