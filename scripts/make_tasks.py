from pathlib import Path
import shutil
import os


project_folder = Path(__file__).parent.parent
tasks_folder = project_folder / "tasks"
docs_folder = project_folder / "docs" / "tasks"

for file in tasks_folder.rglob("Readme.md"):
    task_name = file.parent.name
    shutil.copy(file, docs_folder / (task_name + ".md"))

for task in tasks_folder.iterdir():
    deploy_dir = project_folder / "deploy" / task.name
    shutil.rmtree(deploy_dir)
    deploy_dir = shutil.copytree(task, deploy_dir)
    os.chdir(deploy_dir)
    os.system("git init && git add . && git commit -m 'Initial commit' && git branch -M main")
    os.system(f"git remote add origin git@github.com:mostly-harmless-ai/{task.name}.git")
    os.system(f"git push -f origin main")
