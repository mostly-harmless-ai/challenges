from pathlib import Path
import shutil
import os


def rewrite(file: Path):
    lines = []
    state = "normal"

    with file.open() as fp:
        for line in fp:
            if ":solution:" in line:
                state = "solution"
            elif ":end:" in line:
                state = "normal"

            if state == "normal" and not ":end:" in line:
                lines.append(line)

    with file.open("w") as fp:
        for line in lines:
            fp.write(line)


project_folder = Path(__file__).parent.parent.absolute()

print("PROJECT FOLDER", project_folder)

tasks_folder = project_folder / "tasks"
docs_folder = project_folder / "docs" / "tasks"

for file in tasks_folder.rglob("Readme.md"):
    task_name = file.parent.name
    shutil.copy(file, docs_folder / (task_name + ".md"))

for task in tasks_folder.iterdir():
    deploy_dir = project_folder / "deploy" / task.name
    print("DEPLOY DIR", deploy_dir)
    shutil.rmtree(deploy_dir, ignore_errors=True)

    os.chdir(deploy_dir.parent)
    os.system(f"git clone https://github.com/mostly-harmless-ai/{task.name}.git")

    for fname in deploy_dir.iterdir():
        if fname.name == ".git":
            continue

        if fname.is_file():
            fname.unlink()
        else:
            shutil.rmtree(fname)

    os.chdir(task.name)
    shutil.copytree(task, deploy_dir, dirs_exist_ok=True)
    shutil.copy2(project_folder / ".gitignore", deploy_dir / ".gitignore")

    for fname in deploy_dir.rglob("*.py"):
        rewrite(fname)

    os.system("git add . && git commit -m 'Deployed' && git push origin main")
