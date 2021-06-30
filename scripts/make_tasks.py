from pathlib import Path
import shutil
import os


project_folder = Path(__file__).parent.parent.absolute()
tasks_folder = project_folder / "tasks"
docs_folder = project_folder / "docs" / "tasks"

for file in tasks_folder.rglob("Readme.md"):
    task_name = file.parent.name
    shutil.copy(file, docs_folder / (task_name + ".md"))

for task in tasks_folder.iterdir():
    deploy_dir = project_folder / "deploy" / task.name
    shutil.rmtree(deploy_dir, ignore_errors=True)

    os.chdir(deploy_dir.parent)
    os.system(f"git clone git@github.com:mostly-harmless-ai/{task.name}.git")

    for fname in deploy_dir.iterdir():
        if fname.name == ".git":
            continue

        if fname.is_file():
            fname.unlink()
        else:
            shutil.rmtree(fname)

    os.chdir(task.name)
    shutil.copytree(task, deploy_dir, dirs_exist_ok=True)

    os.system("git add . && git commit -m 'Deployed'")
    os.system(f"git push origin main")
