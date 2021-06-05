# CLOUD COMPUTING PROJECT SOURCE CODE

## 1. Overview

---

This repository contains some scripts written in Python for the purpose of showcasing some features of SparkSQL.

There are 3 scripts:

- __wordcount__: count the number of words in a text file
- __lookup__: provided a date in this format `dd/mm/yyyy`, list out the songs in the Billboard TOP 100 in the respective week
- __stat__: using the Billboard dataset, sort the artists by the number of time that they enter the top 20

## 2. Usage guide

---

### 2.1. Prerequisite

Install the following softwares:

- Python3
- Pip package manager for Python
- Install Pyspark with the command `pip install pyspark`

### 2.2. Running the scripts

Follow these steps to run the scripts:

1. Clone this repo to a folder of your choice
2. Open a terminal (Cmd or Powershell on Windows) and navigate to the chosen folder
3. Navigate into the __src/__ folder
4. Execute script: `python3 <script-name> <args>`

### 2.3. Scripts usage

#### 2.3.1. wordcount

Usage: `python3 wordcount.py <path-to-file>`

#### 2.3.2. lookup

Usage: `python3 lookup.py <date>`

Note: the date for the argument ___must___ be in this format: dd/mm/yyyy

#### 2.3.3. stat

Usage: `python3 stat.py`
