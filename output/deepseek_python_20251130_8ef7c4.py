#!/usr/bin/env python3
"""
Универсальный установщик пакетов для AI/ML разработки
Специально оптимизирован для Python 3.10
"""

import sys
import subprocess
import importlib
import os
import platform
from pathlib import Path

def check_python_version():
    """Проверяет версию Python"""
    required = (3, 10)
    current = sys.version_info
    
    print(f"🐍 Текущая версия Python: {sys.version}")
    
    if current < required:
        print(f"❌ Требуется Python {required[0]}.{required[1]} или выше!")
        print("Скачайте с: https://www.python.org/downloads/")
        return False
    elif current > required:
        print(f"⚠️  У вас новее чем Python {required[0]}.{required[1]}, возможны несовместимости")
    else:
        print("✅ Версия Python 3.10 - оптимальна для установки!")
    
    return True

def run_command(cmd, description):
    """Выполняет команду и выводит результат"""
    print(f"\n🔧 {description}...")
    print(f"Команда: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              capture_output=True, text=True, encoding='utf-8')
        if result.stdout:
            print(f"Вывод: {result.stdout}")
        print(f"✅ Успешно: {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при {description}: {e}")
        if e.stderr:
            print(f"Ошибка: {e.stderr}")
        return False

def check_package(package_name):
    """Проверяет установлен ли пакет"""
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def get_platform_specific_packages():
    """Возвращает пакеты специфичные для платформы"""
    system = platform.system().lower()
    
    base_packages = [
        # Основные для AI/ML
        "numpy", "scipy", "pandas", "scikit-learn",
        # Глубокое обучение (оптимизировано для Python 3.10)
        "tensorflow",  # TensorFlow 2.10+ хорошо поддерживает Python 3.10
        "torch", 
        "torchvision",
        "torchaudio",
        # Визуализация
        "matplotlib", "seaborn", "plotly",
        "bokeh",
        # Разработка
        "jupyter", "jupyterlab", "ipykernel",
        "ipywidgets",
        # Утилиты
        "joblib", "opencv-python", "pillow",
        "psutil", "tqdm",
        # Веб-фреймворки
        "flask", "fastapi", "streamlit",
        # Работа с данными
        "requests", "beautifulsoup4", "lxml",
        "scrapy",
        # Дополнительные ML инструменты
        "xgboost", "lightgbm", "catboost",
        "transformers", "datasets",
        # Оптимизация производительности
        "numba", "cython"
    ]
    
    # Пакеты специфичные для Windows
    if system == "windows":
        base_packages.extend([
            "pywin32",
        ])
    
    # Пакеты специфичные для Linux
    elif system == "linux":
        base_packages.extend([
            "python3-tk",  # для matplotlib
        ])
    
    # Пакеты специфичные для MacOS
    elif system == "darwin":
        base_packages.extend([
            # Дополнительные пакеты для Mac
        ])
    
    return base_packages

def install_with_fallback(package, description):
    """Устанавливает пакет с fallback-вариантами при ошибках"""
    # Базовая попытка установки
    if run_command(f"pip install {package}", f"Установка {description}"):
        return True
    
    # Попытка установки с обновлением pip
    print(f"🔄 Повторная попытка установки {package}...")
    if run_command(f"pip install --upgrade pip && pip install {package}", 
                   f"Повторная установка {description}"):
        return True
    
    # Попытка установки без зависимостей
    print(f"⚠️  Установка {package} без зависимостей...")
    if run_command(f"pip install --no-deps {package}", 
                   f"Установка {description} без зависимостей"):
        return True
    
    print(f"❌ Не удалось установить {package}")
    return False

def create_environment_check():
    """Создает скрипт для проверки окружения"""
    check_script = '''
import sys
import platform

print("=" * 60)
print("ПРОВЕРКА ОКРУЖЕНИЯ AI/ML")
print("=" * 60)

print(f"Python версия: {sys.version}")
print(f"Платформа: {platform.platform()}")

# Проверка ключевых пакетов
packages = [
    ("NumPy", "numpy"),
    ("Pandas", "pandas"), 
    ("Scikit-learn", "sklearn"),
    ("TensorFlow", "tensorflow"),
    ("PyTorch", "torch"),
    ("Matplotlib", "matplotlib"),
    ("Jupyter", "jupyter"),
]

print("\\n📦 ПРОВЕРКА ПАКЕТОВ:")
all_ok = True
for name, package in packages:
    try:
        __import__(package)
        version = getattr(__import__(package), '__version__', 'unknown')
        print(f"✅ {name}: {version}")
    except ImportError:
        print(f"❌ {name}: НЕ УСТАНОВЛЕН")
        all_ok = False

print("\\n" + "=" * 60)
if all_ok:
    print("🎉 ВСЕ ПАКЕТЫ УСТАНОВЛЕНЫ УСПЕШНО!")
    print("💡 Среда готова для работы с NeuroCore!")
else:
    print("⚠️  Некоторые пакеты не установились")

# Проверка GPU
try:
    import tensorflow as tf
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"🎮 Доступно GPU: {len(gpus)}")
        for gpu in gpus:
            print(f"   - {gpu}")
    else:
        print("🎮 GPU: не обнаружено (будет использоваться CPU)")
except:
    print("🎮 Проверка GPU: не удалось выполнить")

print("=" * 60)
'''

    script_path = Path("check_environment.py")
    script_path.write_text(check_script, encoding='utf-8')
    return script_path

def install_packages():
    """Основная функция установки пакетов"""
    
    print("🚀 Начало установки всех пакетов для AI/ML на Python 3.10")
    print("=" * 60)
    
    # Получаем пакеты для текущей платформы
    packages = get_platform_specific_packages()
    
    print(f"📦 Будут установлены {len(packages)} пакетов:")
    for i, package in enumerate(packages, 1):
        print(f"  {i:2d}. {package}")
    
    # Обновление pip и установка wheel
    run_command("python -m pip install --upgrade pip", "Обновление pip")
    run_command("pip install wheel setuptools", "Установка базовых утилит")
    
    # Установка пакетов в несколько проходов
    critical_packages = ["numpy", "scipy", "pandas"]
    ml_packages = [p for p in packages if p not in critical_packages]
    
    print("\n📦 Установка критически важных пакетов...")
    for package in critical_packages:
        install_with_fallback(package, package)
    
    print("\n📦 Установка остальных пакетов...")
    for package in ml_packages:
        install_with_fallback(package, package)
    
    # Специальные команды для совместимости
    print("\n🔧 Оптимизация для Python 3.10...")
    run_command("pip install --upgrade protobuf", "Обновление protobuf")
    run_command("pip install typing-extensions", "Обновление типизации")
    
    return True

def main():
    """Основная функция"""
    print("🤖 Универсальный установщик AI/ML пакетов для Python 3.10")
    print("=" * 60)
    
    # Проверка версии Python
    if not check_python_version():
        sys.exit(1)
    
    # Запуск установки
    success = install_packages()
    
    # Создание скрипта проверки
    check_script = create_environment_check()
    print(f"\n📄 Создан скрипт проверки: {check_script}")
    
    # Создание скрипта активации
    if os.name != 'nt':  # Unix системы
        activation_script = '''#!/bin/bash
echo "🔍 Проверка окружения AI/ML..."
python check_environment.py

echo ""
echo "🚀 Запуск Jupyter Lab..."
jupyter lab
'''
        script_path = Path("start_ai_env.sh")
        script_path.write_text(activation_script, encoding='utf-8')
        script_path.chmod(0o755)
        print(f"📄 Создан скрипт запуска: {script_path}")
    else:  # Windows
        bat_script = '''@echo off
echo 🔍 Проверка окружения AI/ML...
python check_environment.py

echo.
echo 🚀 Запуск Jupyter Lab...
jupyter lab

pause
'''
        Path("start_ai_env.bat").write_text(bat_script, encoding='utf-8')
        print("📄 Создан скрипт запуска: start_ai_env.bat")
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 УСТАНОВКА ЗАВЕРШЕНА!")
        print("\n💡 Дальнейшие действия:")
        print("1. Проверить окружение: python check_environment.py")
        print("2. Запустить среду: start_ai_env.bat (Windows) или ./start_ai_env.sh (Linux/Mac)")
        print("3. Начать работу с NeuroCore: python sim_neurocore.py")
    else:
        print("⚠️ Возникли проблемы при установке")
        print("💡 Попробуйте запустить скрипт от имени администратора")
    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()