# lr2_variant14_complex

Основной проект лабораторной работы №2: консольное приложение, локальный модуль `sorting` и **подмодуль** `matrix_module` (подключаемый репозиторий).

## Структура (после добавления submodule)

- `main.py` — запуск, меню;
- `sorting.py` — сортировки;
- `matrix_module/` — подмодуль (git submodule), внутри — только библиотека матриц, без `main.py`;
- `README.md`, `.gitignore`;
- при submodule появляется ещё `.gitmodules`.

## Подключение подмодуля

```text
git submodule add https://github.com/mDAVIDm2/lr2_variant14_matrix_module.git matrix_module
git submodule update --init --recursive
```

Если клонировали репозиторий без submodules, выполните `git submodule update --init --recursive` в корне `lr2_variant14_complex`.

## Запуск

```text
cd lr2_variant14_complex
python main.py
```

Без папки `matrix_module` приложение сообщит, что нужно инициализировать submodule (или вручную клонировать репозиторий в каталог `matrix_module` с тем же содержимым, что в `lr2_variant14_matrix_module`).
