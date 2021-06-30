# Hello World

The purpose of this task is to get you started with the setup necessary for participating in the remaining challenges.
As such, there is no real exercise here.
We will focus instead on learning the workflow for participating on a task, submitting your code, and getting it evaluated.
This task is also a guide for contributors designing new challenges.

## Prerequisites

To participate in this task you'll just need a standard installation of Python.
Instructions for installing Python in multiple in architectures is available on [their website](https://python.org/installation).
Additionally, you'll need to create a [Github account](https://github.com/signup), and install [Git](https://git-scm.org) on your terminal.

These prerequisites are the minimum necessary for every other challenge.

## Setting up the coding environment

The next step is to navigate to [this task's repository in Github](https://github.com/mostly-harmless-ai/task-hello-world).
On the top right corner of the main window you'll see a button titled `Fork`; click on it.
Now follow the instructions and you'll have your own copy of the challenge in your own Github namespace.

Once forked, you can clone your own copy of the repository.
If your Github username is `user`, you can achieve this by typing the following on a terminal:

    git clone https://github.com/user/task-hello-world

Now you can open this folder on your desired editor.
You should see a `Readme.md` file with these same instructions, and some other files we'll go over in a minute.

It's time to set up your coding environment.
The first step will be to create a separate virtual environment.
This will ensure that whatever library you need to install for this specific task will not mess up with your standard Python installation.
If you don't know what is a virtual environment or how to create one, you can read more [here]().

Once you're safely inside your isolated environment, you can install the dependencies for this task by typing the following in the terminal, while located on the root folder of the task~(the one that contains the `Readme.md` file).

    pip install -r requirements.txt

> 📝 If you prefer a different way of isolating your environment~(e.g., using Docker, conda environments, pyenv, Poetry, etc.) you are free to do so as well.

## Adding your code
