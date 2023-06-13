## About
This is a basic attempt to understand modern Python package and environment management using Poetry.

### Tools used
- pyenv
- poetry
- pytest
- dotenv


# Python setup (MAC)

### Setup Pyenv

```bash
brew install openssl readline sqlite3 xz zlib
```

```bash
brew update
```

```bash
brew install pyenv
```

### For ZSH

```bash
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
```

## INSTALLING PYTHON

```bash
# this will give the already installed versions of Python on your system
pyenv versions

# to install a specific version
pyenv install 3.11.1

# to **set a specific version** as global from the available list
pyenv global 3.11.1

```

### check in a new terminal

```bash
➜  ~ python -V
Python 3.11.1
➜  ~ pyenv versions
  system
* 3.11.1 (set by /Users/subhranshu/.pyenv/version)
```

### INSTALLING POETRY

**Reference Video** - 
https://www.youtube.com/watch?v=0f3moPe_bhk

Since we have `pyenv` , `pip` is automatically understood to use which version

```bash
pip poetry
```

### add this to the .zshrc file

```bash
export PATH=$PATH:$HOME/.poetry/bin
```

then hit

```bash
source ~/.zshrc
# best practice is to start working on a new terminal after this step
```

## SETTING UP A NEW PYTHON PROJECT WITH POETRY

### if you are using PYENV, do this before anything

```bash
poetry config virtualenvs.prefer-active-python true
```

### setup the virtual environment inside the current project directory

```bash
poetry config virtualenvs.in-project true
```

### to check the POETRY config in the terminal

```bash
poetry config --list
```

## now create a project

```bash
poetry init

# go through the interactive CLI to generate the "pyproject.toml" file

poetry install
```


<aside>
💡 We will have the following -
“.venv”
poetry.lock

</aside>


## Running the VIRTUAL ENV in the CLI

```bash
poetry shell
```

We get something like below. If you notice, the VENV is pointing to the current project directory’s **`.venv`** directory

```bash
➜  mypylib poetry shell
Spawning shell within /Users/subhranshu/Desktop/projects/mypylib/.venv
➜  mypylib emulate bash -c '. /Users/subhranshu/Desktop/projects/mypylib/.venv/bin
/activate'
(mypylib-py3.11) ➜  mypylib
```

<aside>
💡 Now you can **run the Python program in this shell** so that your python code runs in this Poetry managed virtual environment.

</aside>

### Sample Code

```python
import requests

print("hello poetry!!")
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
response_json = response.json()
print(response_json["title"])
```

**IN THE CLI**

```bash
(mypylib-py3.11) ➜  mypylib python app.py
hello poetry!!
delectus aut autem
(mypylib-py3.11) ➜  mypylib
```

# ANOTHER WAY

```bash
poetry new --name pysandbox --src pysandbox
```

```bash
poetry install
```

This creates the below structure-

```bash
➜  pysandbox tree
.
├── README.md
├── poetry.lock
├── pyproject.toml
├── src
│   └── pysandbox
│       └── __init__.py
└── tests
    └── __init__.py

4 directories, 5 files
```

create a `.gitignore` file

```bash
.venv
.env
**/**/__pycache__/**
*.pyc
```

<aside>
💡 Make sure to create this file, else you might have to manually `rm -rf` the pycache directories and then `git commit`

</aside>

Add `pytest` for running tests

```bash
poetry add pytest --group dev
```

create a test file `test_adder.py`  for the `src/adder.py` file

```bash
import unittest
from pysandbox.adder import add, addBy100

class AdderTest(unittest.TestCase):

    def test_add_should_add_two_numbers(self):
        a = 20
        b = 40
        self.assertEqual(add(a, b), 60)

    def test_add_by_100_should_add_100(self):
        a = 40
        b = 80
        self.assertEqual(addBy100(a, b), 220)
    

if __name__ == "__main__":
    unittest.main()
```

### we can run `pytest` in the poetry shell to see the test results.

## Using `python-dotenv` to load ENV variables

```bash
poetry add python-dotenv --group dev
```

create a `profile.py`

```bash
import os
from dotenv import load_dotenv

# load ENV variables using load_dotenv()
load_dotenv()

profile = os.getenv("APP_PROFILE")
print(f"the Python app is for '{profile}'")
```

create a ENV variable in the `.env` file

```bash
APP_PROFILE=beginner
```

RUN the program

```bash
(pysandbox-py3.11) ➜  pysandbox git:(main) ✗ python src/pysandbox/profile.py

# output
the Python app is for 'beginner'
(pysandbox-py3.11) ➜  pysandbox git:(main) ✗
```


