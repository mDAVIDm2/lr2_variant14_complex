# -*- coding: utf-8 -*-
"""
Основное приложение: сортировка (локальный модуль) и работа с матрицей (подмодуль).
"""
from sorting import bubble_sort


def run_matrix_demo() -> None:
    try:
        from matrix_module import (
            diagonal_sums,
            determinant,
            minimum_element,
        )
    except ImportError:
        print("Нет пакета matrix_module.")
        print("Выполните: git submodule add https://github.com/mDAVIDm2/lr2_variant14_matrix_module.git matrix_module")
        print("или: git submodule update --init --recursive")
        return

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s2 = [[2, 1], [5, 3]]
    main_s, sec_s = diagonal_sums(m)
    v, r, c = minimum_element(m)
    print("Матрица 3x3:", m)
    print("  Сумма главной диагонали:", main_s, "  побочной:", sec_s)
    print("  Определитель 3x3:", determinant(m))
    print("  Мин. элемент:", v, f"({r}, {c})")
    print("Матрица 2x2:", s2, "  det:", determinant(s2))


def run_sorting_demo() -> None:
    raw = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Список:", raw)
    print("После bubble_sort:", bubble_sort(raw))


def main() -> None:
    while True:
        print(
            """
=== Вариант 14 (complex) ===
 1 — демо сортировки (sorting.bubble_sort)
 2 — демо матриц (подмодуль matrix_module)
 0 — выход
            """.strip()
        )
        c = input("Выбор: ").strip()
        if c == "0":
            break
        if c == "1":
            run_sorting_demo()
        elif c == "2":
            run_matrix_demo()
        else:
            print("Неизвестный пункт.")


if __name__ == "__main__":
    main()
    try:
        input("\nEnter — выход...")
    except EOFError:
        pass
