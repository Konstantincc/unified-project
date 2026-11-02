r"""
Unified Project Launcher — меню для запуска подпроектов.
Запуск: .\.venv\Scripts\python.exe main.py
r"""
import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

PROJECTS = {
    "1": ("Django — myproject (runserver)",  ROOT / "myproject",                     "runserver"),
    "2": ("AI — my_ai_project",              ROOT / "my_ai_project",                 "src/models.py"),
    "3": ("Qiskit Networks — BB84 demo",     ROOT / "qiskit-networks",               "docs/demo/discrete_bb84/network.py"),
    "4": ("SpikeNN — run",                   ROOT / "SpikeNN",                       "app/run.py"),
    "5": ("Teleportation (нет entrypoint)",  ROOT / "Quantum-Teleportation",         None),
    "6": ("QCT — Code QCT",                  ROOT / "Quantum_Coherent_Transport-",   "Code QCT.py"),
    "7": ("Routing Simulation",              ROOT / "Quantum-Routing-Simulation",    "protocol-simulation.py"),
    "8": ("output — deepseek script",        ROOT / "output",                        "deepseek_python_20251130_8ef7c4.py"),
}

def run_project(key: str):
    name, proj_dir, entry = PROJECTS[key]
    print(f"\n▶ {name}")
    print(f"  Папка: {proj_dir}")

    if not proj_dir.exists():
        print("  ❌ Папка не существует")
        return

    if entry is None:
        print("  ℹ️  Нет точки входа — откройте файлы вручную")
        return

    # ВАЖНО: Django-специфичный случай проверяем ДО проверки файла
    if entry == "runserver":
        print("  Команда: manage.py runserver")
        os.chdir(proj_dir)
        subprocess.run([sys.executable, "manage.py", "runserver"])
        return

    target = proj_dir / entry
    if not target.exists():
        print(f"  ❌ Файл не найден: {target}")
        return

    print(f"  Файл: {target}")
    os.chdir(proj_dir)
    subprocess.run([sys.executable, entry])

def menu():
    print("\n" + "=" * 58)
    print("  Unified Project Launcher")
    print("=" * 58)
    for key, (name, _, _) in PROJECTS.items():
        print(f"  {key}) {name}")
    print("  0) Выход")
    print("=" * 58)

def main():
    while True:
        menu()
        choice = input("Выбор: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        if choice in PROJECTS:
            try:
                run_project(choice)
            except KeyboardInterrupt:
                print("\n  ⏹ Прервано")
            except Exception as e:
                print(f"  ❌ {type(e).__name__}: {e}")
            input("\nEnter — вернуться в меню...")
        else:
            print("  ❌ Нет такого пункта")

if __name__ == "__main__":
    main()