import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory(directory_path: str):
    try:
        # Перетворення шляху на Path-об'єкт
        dir_path = Path(directory_path)

        # Перевірка, чи шлях існує і є директорією
        if not dir_path.exists():
            print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує.")
            return
        if not dir_path.is_dir():
            print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не є директорією.")
            return
        
         # Функція для рекурсивного обходу директорій
        def traverse_dir(path: Path, indent: int = 0):
            for item in path.iterdir():
                if item.is_dir():
                    print(f"{' ' * indent}{Fore.BLUE}[Директорія] {item.name}")
                    traverse_dir(item, indent + 4)
                else:
                    print(f"{' ' * indent}{Fore.GREEN}[Файл] {item.name}")

        # Виведення структури директорії
        print(f"{Fore.CYAN}Структура директорії '{directory_path}':")
        traverse_dir(dir_path)
        

    except Exception as e:
        print(f"{Fore.RED}Виникла помилка: {e}")


if __name__ == "__main__":
    # Перевірка аргументів командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Використання: python main.py <шлях_до_директорії>")
    else:
        visualize_directory(sys.argv[1])

