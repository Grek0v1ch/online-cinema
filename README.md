# Online cinema 

👋🏻 Welcome to the Online cinema  Project repository!
This project is dedicated to microservice for online cinema!
## Quick Links

1. [Project Overview](#project-overview)
2. [Folder Structure Explained](#folder-structure-explained)
5. [Usage](#usage)

---

## Project Overview

The main goal of this project is to write and configure microservices that interact with each other for an online cinema.
## Folder Structure Explained

The project's folder structure is designed for clarity and modularity. Here's an overview of the key folders and their contents:

- **cinema-library**: microservice for working with movies.
- **users**: microservice for working with users.
- **protobufs**: It contains special *.proto files designed to create source code for clients and servers.
- **cinema-app**: microservice for working through the web interface, connects the "cinema-library" and "users".



## Usage
The entire project can be executed either in a Docker container or without it.

- **Building and run the Docker**:

    ```bash
    docker-compose up
    ```
- **Run without the Docker**:
1. Run cinema-librarry

    ```bash
    python main.py 
    ```
2. Run users

    ```bash
    python main.py 
    ```
3. Run cinema-app
- if you are using Mac OS or Linux, then you can run the application as follows:
    ```bash
  FLASK_APP=main.py flask run
    ```
- if you are using Windows, then you can run the application as follows::
  ```
  set FLASK_APP=main.py // $env:FLASK_APP = "main.py"
  flask main.py
  ```