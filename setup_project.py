import os

folders = [
    "data/raw", "data/processed", "notebooks", "src", "app", "outputs/models",
    "outputs/figures", "outputs/logs", "tests"
]
files = ["README.md", "requirements.txt", ".gitignore", "app/app.py"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("Project structure created!")