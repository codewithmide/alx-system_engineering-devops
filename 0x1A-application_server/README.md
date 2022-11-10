# 0x1A. Application server
`DevOps` `SysAdmin`

|By: Sylvain Kalache, co-founder at Holberton School|
|:--|
|Weight: 1|
|Project will start Nov 7, 2022 6:00 AM, must end by Nov 11, 2022 6:00 AM|
|was released at Nov 9, 2022 8:24 PM|
|An auto review will be launched at the deadline|

## Concepts
For this project, we expect you to look at these concepts:

- [Web Server](https://alx-intranet.hbtn.io/concepts/17)
- [Server](https://alx-intranet.hbtn.io/concepts/67)
- [Web stack debugging](https://alx-intranet.hbtn.io/concepts/68)

## Background Context


Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## Resources
**Read or watch:**

- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)](https://docs.gunicorn.org/en/latest/run.html)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
- [Upstart documentation](https://upstart.ubuntu.com/cookbook/)

## Requirements
### General
- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

## Bash Scripts
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
