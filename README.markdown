Modifications of Foldiak's Algorithm for Imbalanced Data
=====================================

___Authors___  
* Luke E. Bemish `<lukebemish@gmail.com>`
* Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Overview][#1]

   1.1. [Software Dependencies][#1.1]

   1.2. [Directory Structure][#1.2]

2. [Usage][#2]

   2.1. [Setting Up][#2.1]

3. [References][#3]

------------------------------------------------------------------------------

## 1. Overview

This project contains a modified version of [Foldiaks Algorithm][#foldiakalg] allowing the bit probabilities of output nodes to change and adapt to the data.

### 1.1 Software Dependencies

#### Base Requirements

* Python

#### Required Python Packages ####

* `numpy`
* `numba`
* `scipy`

### 1.2 Directory Structure

    README.markdown
    requirements.txt
    config/
    data/
    tests/
    lib/

* `README.markdown`: this file

* `requirements.txt`: `pip` requirements file containing Python packages necessary for this code to run

* `config`: directory containing template configuration files (e.g., `autoenv`
  configuration file)

* `data`: directory where data is generated by example or test scripts.

* `tests`: directory containing minimal examples of working code. For more examples and notebooks used during develpoment, see the `dev` branch of the repository.

* `lib`: directory containing library code.

## 2. Usage

### 2.1 Setting Up

* Create Python virtual environment for project.

    ```bash
    $ mkvirtualenv -p /PATH/TO/PYTHON PROJECT_NAME
    ```

* Install required Python packages.

    ```bash
    $ pip install -r requirements.txt
    ```

* Set up autoenv.

  - Copy `config/env` to `.env` in project root directory.

  - Set template variables in `.env` (indicated by `{{ }}` notation).
  
  - This is not strictly necessary; the code should run fine without autoenv configured (and even without virtualenv) as long as everything else is set up.

------------------------------------------------------------------------------

* Make sure the `lib` folder is in your `sys.path` or `PYTHONPATH`. One way to do this would be to put its path in a `.pth` file inside the `site-packages`.

## 3. References
------------

* P. Földiák.
  ["Forming sparse representations by local anti-Hebbian learning"][#foldiakalg]
  (1990/12).

------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview
[#1.1]: #11-software-dependencies
[#1.2]: #12-directory-structure

[#2]: #2-usage
[#2.1]: #21-setting-up

[#3]: #3-references

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[#foldiakalg]:
  https://doi.org/10.1007/BF02331346
