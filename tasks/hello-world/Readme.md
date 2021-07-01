# Hello World

The purpose of this task is to get you started with the setup necessary for participating in the remaining challenges.
As such, there is no real exercise here.
We will focus instead on learning the workflow for participating on a task, submitting your code, and getting it evaluated.

## Prerequisites

To participate in this task you'll just need a standard installation of Python.
Instructions for installing Python in multiple in architectures is available on [their website](https://python.org/installation).
Additionally, you'll need to create a [Github account](https://github.com/signup), and install [Git](https://git-scm.org) on your terminal.

These prerequisites are the minimum necessary for every other challenge.

## Setting up the coding environment

Navigate to [this task's repository in Github](https://github.com/mostly-harmless-ai/hello-world).
On the top right corner of the main window you'll see a button titled `Fork`; click on it.
Follow the instructions and you'll have your own copy of the challenge in your own Github namespace.

Once forked, you can clone your own copy of the repository.
If your Github username is `user`, you can achieve this by typing the following on a terminal:

    git clone https://github.com/user/hello-world

Open the  `hello-world` folder on your desired editor.
You should see a `Readme.md` file with these same instructions, and some other files we'll go over in a minute.

It's time to set up your coding environment.
The first step will be to create a separate virtual environment.
This will ensure that whatever library you need to install for this specific task will not mess up with your standard Python installation.
If you don't know what is a virtual environment or how to create one, you can read more [here]().

Once you're safely inside your isolated environment, you can install the dependencies for this task by typing the following in the terminal, while located on the root folder of the task~(the one that contains the `Readme.md` file).

    pip install -r requirements.txt

> 📝 If you prefer a different way of isolating your environment~(e.g., using Docker, conda environments, pyenv, Poetry, etc.) you are free to do so as well.

## Task description

Now you're ready to start hacking your solution!
In a real task, this is the point where you do all the heavy work.
In this task, though, since we're only concerned with learning the workflow, we crafted a silly exercise for you.

Open `hello_world.py` and modify the method called `answer` so that it reads:

```python
def answer():
    return 42
```

That's it! Bonus points if you get the joke 😆.

## Checking your code

If you installed the required dependencies, you should be able to run:

    pytest

And get a pretty green message saying everything is OK!

## Submitting your code

Once solved and tested locally, you're ready to push your code.
Start by pushing to your own fork, this should be as easy as:

    git push origin main

Go to your task fork in Github and look for the `Contribute` menu just under the green `Code`button.
Click it and then click on `Create pull request`.
Follow the instructions. On the description field, write a brief description about your solution.

Wait for the Github CI to kick in, and run the tests.
If you need help or feel stucked, just add a comment on the PR.

## Get a badge!

Once all tests have passed, this means your solution has been checked.
One or more mentors from the community will come over and review your code, helping you improve it beyond passing the tests, commenting on best practices or ideas for alternative solutions.

Once you're comfortable with your solution, ask a mentor to evaluate it.
They will assign a `SUCCESS` label to your pull-request, and close it.
