### Hexlet tests and linter status:
[![Actions Status](https://github.com/hwarz/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/hwarz/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8136a514e6c01bab3537/maintainability)](https://codeclimate.com/github/hwarz/python-project-49/maintainability)

  <h3 align="center">BRANE GAMES</h3>

  <p align="center">
    A Hexlet Students First Python Project

## Built With

Languages/frameworks/libraries used to bootstrap the project.

[![](https://img.shields.io/badge/language-python-blue)](https://github.com/topics/python) [![](https://img.shields.io/badge/library-prompt-%23EE7D0D)](https://github.com/topics/prompt) [![](https://img.shields.io/badge/library-random-black)](https://github.com/topics/random) [![](https://img.shields.io/badge/library-math-success)](https://github.com/topics/math)

## Dependencies
Dependencies for correct working of the code:

- python = "^3.9"
- prompt = "^0.4.1"

## Description

**"Brain Games"** is a set of five console games. After three correct answers, the game is considered to be over. The wrong answer ends the game and offers to play it again.

*Games:*
- Brain Even - Answer "yes" if the number is even, otherwise answer "no"
- Brain Calculator - Answer what is the result of the expression.
- Brain GCD - Answer what is the greatest common divisor of given numbers.
- Brain Progression - Answer what number is missing in the progression.
- Brain Prime - Answer "yes" if given number is prime, otherwise answer "no".

You can open it with this commands:
```bash
>> brain-even
>> brain-calc
>> brain-gcd
>> brain-progression
>> brain-prime
```
The first project introduces the basic steps: installing the language, setting up the environment (operating system, editor, linters), connecting additional libraries, creating a git repository. The utility Poetry is needed for: installing and upgrading additional libraries, publishing packages, and much more. The linter (flake8) automatically monitors the code style and finds potential errors. Another powerful element of real-world development is continuous integration (CI). Such systems are an integral part of any professional development. Github Actions is chosen as a free and Github-integrated build system. The main issue in the project is the architecture. Games have a common order of execution: ask a question, get an answer, compare the answer, and so on. This logic was moved to one place and reused inside specific games to eliminate code duplication. 

### Summary
* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Demo](#demo)
  * [Brain Even](#Brain Even:)
  * [Brain Calculator](#brain-calc)
  * [Brain GCD](#brain-gcd)
  * [Brain Progression](#brain-progression)
  * [Brain Prime](#brain-prime)
* [Development](#development)
  * [Dev Dependencies](#dev-dependencies)
  * [Project Organization](#project-organization)
  * [Useful commands](#useful-commands)

___

## Installation

### Python
Before installing the package, you need to make sure that you have Python version 3.9 or higher installed:

```bash
# Windows, Ubuntu, MacOS:
>> python --version # or python -V
Python 3.9.0+
```
### Poetry
The command for installing the program into your operating system:
https://python-poetry.org/docs/#installing-with-pipx . The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry provides a custom installer that will install poetry isolated from the rest of your system by vendorizing its dependencies. This is the recommended way of installing poetry.

Once Poetry is installed and in your $PATH, you can execute the following:
```bash
>> poetry --version
```
### Project package
To work with the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project on the command line:
```bash
# clone via SSH:
>> git clone git@github.com:hwarz/python-project-49.git
```

It remains to move to the directory and install the package:

```bash
>> cd python-project-49
>> poetry build
>> python3 -m pip install --user dist/*.whl
# If you have previously installed a package and want to update it, use the following command:
# >> python3 -m pip install --user --force-reinstall dist/*.whl
```
### Demo
#### Brain Even:
The user is shown a random number. And he has to answer yes if the number is even, or no if it is odd:
**Examples:**
```bash
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
>> Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.

Answer "yes" if the number is even, otherwise answer "no".
Question: 15
>> Your answer: no
Correct!
```
[![asciicast](https://asciinema.org/a/yy8f2inVomXQVXpGFL4hpbr34.svg)](https://asciinema.org/a/yy8f2inVomXQVXpGFL4hpbr34)

#### :video_game: Brain Calculator:
`brain-calc`

The user is shown a random mathematical expression, such as 87 + 48, which must be calculated and write down the correct answer.

**Examples:**
```bash
What is the result of the expression?
Question: 87 + 48
>> Your answer: 126
'126' is wrong answer ;(. Correct answer was '135'.

What is the result of the expression?
Question: 87 + 48
>> Your answer: 135
Correct!
```

[![asciicast](https://asciinema.org/a/6YfLN2LNdCYUgqN9J4JPMULdp.svg)](https://asciinema.org/a/6YfLN2LNdCYUgqN9J4JPMULdp)

#### :video_game: Brain GCD:
`brain-gcd`

The user is shown two random numbers, for example 25 and 50. The user must calculate and enter the greatest common divisor of these numbers.

**Examples:**
```bash
Find the greatest common divisor of given numbers.
Question: 25 50
>> Your answer: 5
'5' is wrong answer ;(. Correct answer was '25'.

Find the greatest common divisor of given numbers.
Question: 25 50
>> Your answer: 25
Correct!
```

[![asciicast](https://asciinema.org/a/oIAdKA0EdrsfnhEsgPx0qSMhE.svg)](https://asciinema.org/a/oIAdKA0EdrsfnhEsgPx0qSMhE)

#### :video_game: Brain Progression:
`brain-progression`

The user is shown a series of numbers with a missing number, forming an arithmetic progression. The player has to determine this number.

**Examples:**
```bash
What number is missing in the progression?
Question: 3 26 .. 72 95 118 141 164 187
>> Your answer: 43
'43' is wrong answer ;(. Correct answer was '49'.

What number is missing in the progression?
Question: 3 26 .. 72 95 118 141 164 187
>> Your answer: 49
Correct!
```

[![asciicast](https://asciinema.org/a/2rz1kwFwNtPljS638duAiTNXX.svg)](https://asciinema.org/a/2rz1kwFwNtPljS638duAiTNXX)

#### :video_game: Brain Prime:
`brain-prime`

The user is shown a random number. And he needs to answer yes if the number is prime, or no if it is composite:

**Examples:**
```bash
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 67
>> Your answer: no
'no' is wrong answer ;(. Correct answer was 'yes'.

Answer "yes" if given number is prime. Otherwise answer "no".
Question: 67
>> Your answer: yes
Correct!
```

[![asciicast](https://asciinema.org/a/HtlDeQjczIjLxiHlE5A12P1wj.svg)](https://asciinema.org/a/HtlDeQjczIjLxiHlE5A12P1wj)

___

## Development

### Dev Dependencies

List of dev-dependencies:
- flake8 = "^4.0.1"

### Project Structure
```bash
.
├── brain_games
│   ├── __init__.py
│   ├── cli.py
│   ├── common_logic.py
│   ├── games
│   │   ├── __init__.py
│   │   ├── calc.py
│   │   ├── even.py
│   │   ├── gcd.py
│   │   ├── progression.py
│   │   └── prime.py
│   └── scripts
│       ├── __init__.py
│       ├── brain_games.py
│       ├── brain_calc.py
│       ├── brain_even.py
│       ├── brain_gcd.py
│       ├── brain_progression.py
│       └── brain_prime.py
├── dist
    ├── hexlet_code-0.1.0-py3-none-any.whl
    ├── hexlet_code-0.1.0.tar.gz 
├── Makefile
├── README.md
├── pyproject.toml
├── poetry.lock
└── setup.cfg
```

### Useful commands

The commands listed in the Makefile:

<dl>
    <dt><code>make install</code></dt>
    <dd>Installing Poetry.</dd>
    <dt><code>make brain-games</code></dt>
    <dd>Installing ther game.</dd> 
    <dt><code>make publish</code></dt>
    <dd>Installing a poetry publish.</dd>
    <dt><code>make package-install</code></dt>
    <dd>Installing a package in the user environment.</dd>
    <dt><code>make build</code></dt>
    <dd>Building the distribution of he Poetry package.</dd>
    <dt><code>make package-force-reinstall</code></dt>
    <dd>Reinstalling the package in the user environment.</dd>
    <dt><code>make lint</code></dt>
    <dd>Checking code with linter.</dd>
</dl>
___

:man_technologist: Author: [@Vladimir Arshba](https://github.com/hwarz/python-project-49)
