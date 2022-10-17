# 0x15. API
`Python` `Scripting` `Back-end` `API`

|By: Sylvain Kalache, co-founder at Holberton School|
|:--|
|Weight: 1|
|Project will start Oct 17, 2022 6:00 AM, must end by Oct 18, 2022 6:00 AM|
|will be released at Oct 17, 2022 12:00 PM|
|An auto review will be launched at the deadline|

# Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources
**Read or watch:**

- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [What is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices](https://smartbear.com/solutions/microservices/)
- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if __name__ == "__main__":)
