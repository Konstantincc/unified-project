# Unified Python Projects

Собрано из пользовательских `.py` файлов на `D:\баловство`.

## Подпроекты

| Проект | Описание | Файлов |
|---|---|---|
| [`myproject/`](myproject/) | Django-сайт | 14 |
| [`my_ai_project/`](my_ai_project/) | AI | 3 |
| [`qiskit-networks/`](qiskit-networks/) | Квантовые сети + BB84 | 24 |
| [`SpikeNN/`](SpikeNN/) | Spiking Neural Network | 16 |
| [`Quantum-Teleportation/`](Quantum-Teleportation/) | qibo + qiskit | 4 |
| [`Quantum_Coherent_Transport-/`](Quantum_Coherent_Transport-/) | QCT | 2 |
| [`Quantum-Routing-Simulation/`](Quantum-Routing-Simulation/) | Маршрутизация | 1 |
| [`output/`](output/) | Скрипт | 1 |

## Быстрый старт

```bash
git clone https://github.com/Konstantincc/unified-project.git
cd unified-project
python -m venv .venv
pip install -r requirements.txt
python main.py
```

## Лаунчер

`main.py` — меню для запуска любого подпроекта.

## CI

GitHub Actions: `.github/workflows/ci.yml` — compile + smoke-import.
