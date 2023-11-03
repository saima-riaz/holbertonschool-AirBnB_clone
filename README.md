# AirBnB Clone - The Console

<div style="text-align:center"><img src="https://github.com/davisjoseph6/holbertonschool-AirBnB_clone/assets/38712815/38712093-1db4-4d05-8d6e-f6fdb9f1d276" /></div>

## Introduction

This is a command-line application designed to manage AirBnB objects, part of a larger project to build an AirBnB clone. The project focuses on creating a command interpreter for various functionalities like creating, retrieving, updating, and destroying objects. The application allows users to interact with objects of various classes, including User, State, City, and Place, and stores the data in a file-based storage system.

## Concepts

- Python packages
- AirBnB clone
- Command-line interface
- Serialization and deserialization
- Unit testing

## Background Context

Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page.

## First Step

The initial step in building the AirBnB clone is to create a command interpreter that manages AirBnB objects. This command interpreter is crucial for the overall functionality of the project. Key tasks include:

- Creating a parent class (BaseModel) to handle the initialization, serialization, and deserialization of instances.
- Establishing a flow of serialization and deserialization from instances to dictionaries to JSON strings to files.
- Creating classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel.
- Developing the first abstracted storage engine (File storage) for the project.
- Implementing unit tests to validate all classes and the storage engine.

## What's a Command Interpreter?

The command interpreter is similar to a command-line shell but is specific to the AirBnB project. It enables users to perform the following actions:

- Create a new object (e.g., User, Place, etc.).
- Retrieve an object from storage.
- Perform operations on objects (e.g., counting, computing statistics).
- Update attributes of an object.
- Delete an object.

<div style="text-align:center"><img src="https://github.com/davisjoseph6/holbertonschool-simple_shell-collaborative/assets/38712815/66466a31-3456-4633-90f7-98edd28281ef" /></div>

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without needing external help:

### General

- Creating a Python package
- Developing a command interpreter in Python using the cmd module
- Understanding unit testing and implementing it in a large project
- Serialization and deserialization of classes
- Reading and writing JSON files
- Managing datetime in Python
- Understanding UUID (Universally Unique Identifier)
- Using '**args'** and '**kwargs'** in Python functions
- Handling named arguments in a function

## Requirements

#### Python Scripts

- Use Python 3.8.5 on Ubuntu 20.04 LTS.
- Ensure all your files end with a new line.
- Start each file with '#!/usr/bin/python3'.
- Include a mandatory README.md file at the project's root folder.
- Adhere to the PEP 8 style guide using pycodestyle (version 2.7.**).**
- Make all your files executable.
- Test file length using wc.
- Document all modules, classes, and functions with meaningful descriptions.

#### Python Unit Tests

- All test files should be inside a folder named tests.
- Use the unittest module for testing.
- Ensure test files and folders start with test_._
- Organize test files in the same structure as the project.
- Run tests using python3 -m unittest discover tests.

### GitHub

- Maintain one project repository per group.
- Avoid cloning, forking, or using a repository with the same name before the second deadline to avoid a 0% score.

## Execution

The command interpreter should work in interactive mode and non-interactive mode. Interactive mode should resemble the following:

<div style="text-align:center"><img src="https://github.com/davisjoseph6/holbertonschool-simple_shell-collaborative/assets/38712815/319724f8-543d-4c89-9453-6f63e501edbe" /></div>

Non-interactive mode allows you to execute commands directly from the command line, like this:

<div style="text-align:center"><img src="https://github.com/davisjoseph6/holbertonschool-simple_shell-collaborative/assets/38712815/8a6151d4-f0d3-4885-9676-3dff2e373f37" /></div>

All tests should also pass in non-interactive mode using the command echo "python3 -m unittest discover tests" | bash.

## Authors
- Coconuts-del 6712@holbertonstudents.com [GitHub](https://github.com/Coconuts-del)
- Davis Joseph davisjoseph767@gmail.com [GitHub](https://github.com/davisjoseph6)
- saima-riaz saimariaz1422@gmail.com [GitHub](https://github.com/saima-riaz)

**Note:** This README provides an overview of the AirBnB clone project and its requirements. Detailed information about specific functionalities, classes, and methods will be available in the project's documentation and codebase.
