# README

## Contents

* Overview
* Grab the code
* Install dependencies
* Run output

---

## Overview

This package contains a small [Python](https://www.python.org) / [Django](https://www.djangoproject.com) API solution to the [RideTo](https://www.rideto.com/) 'products' coding assignment.

The deployed version is available at the following temporary Heroku address: [https://ride-to-api.herokuapp.com](https://ride-to-api.herokuapp.com)

---

## Grab the code

If required, grab (or clone) this package by entering (or copying and pasting) the following code into a terminal:

```bash
# Cd into your home directory
cd ~/

# Grab (or clone) this package locally
# git clone https://github.com/aldersondigital/ride-to-api 
```

In order to run the package's output, please continue with the __Install dependencies__ section of this document below.

---

## Install dependencies

Before running the package's output, please install the required dependencies by entering (or copying and pasting) the following commands into a console / terminal:

```bash
# CD into the directory extracted from the archive.
cd ./ride-to-api/

# Install the required dependencies using [PIP](https://pypi.org/project/pip/)
pip install -r requirements.txt
```

In order to run the package's output, please continue with the __Run output__ section of this document below.

---

## Run output

Once the package's dependencies have been installed, run the output, which will be available at `http://localhost:3000/`, by entering (or copying and pasting) the following command into a console / terminal:

```bash
# CD into the directory extracted from the archive.
cd ./ride-to-api/

# Run the package's output.
python manage.py runserver
```

> Once `python manage.py runserver` has been entered, the output should be available at: `http://localhost:8000/`
