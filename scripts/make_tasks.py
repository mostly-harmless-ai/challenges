from pathlib import Path

project_folder = Path(__file__).parent.parent
tasks_folder = project_folder / "tasks"
docs_folder = project_folder / "docs" / "tasks"

for file in tasks_folder.rglob("Readme.md"):
    task_name = file.parent.name

    with open(docs_folder / (task_name + ".md"), "w") as fp:
        fp.write(file.read_text())
