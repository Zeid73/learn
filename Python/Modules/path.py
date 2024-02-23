from pathlib import Path

p = Path()

for file in p.glob("*.py"):
    print(file)
