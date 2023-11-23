# CRMSIEMSERVER

This Python project provides a FastAPI server that allows you to perform parameterized queries and receive logs from custom Python agents or anything that can send a JSON POST request. It serves as a RESTful API to interact with a MongoDB database and collect logs generated by various sources. With this server, you can easily retrieve data from your database by specifying query parameters and receive real-time logs from agents for monitoring and analysis.

## Features

- **FastAPI Framework:** This project uses FastAPI, a modern web framework for building high-performance APIs with Python.

- **Parameterized Queries:** Easily perform parameterized queries to retrieve data from your database.

- **Custom Python Agent Logs:** Custom Python agents can send logs to the server, providing real-time information for monitoring and analysis.

This is the [link](https://github.com/israsecnet/XufiSIEMClient) to the repository for the client program that can be installed on various systems to serve as a custom log extractor, an EDR agent, as well as the capability for incident response functions and remote administration.


## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- PyMongo (or other database connector of your choice)

## Installation

1. Clone this repository to your local machine.

```
git clone https://github.com/israsecnet/CRMSIEMSERVER.git
```

3. Install the required dependencies using pip

```
pip install -r requirements.txt
```

3. Configure your database connection in `database.py` or create a custom configuration file.

4. Start the FastAPI server.

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

You can change the host and port as needed.

## Usage

### Perform Parameterized Queries

To perform parameterized queries, make a GET request to the following endpoint:

```
http://localhost:8000/query/
```

You can provide query parameters in the request, for example:

```
http://localhost:8000/query?key=MongoDBKey&value=MongoDBVALUE&collec=MongoDBCollection
```
 
### Receive Custom Python Agent Logs

Custom Python agents can send logs to the server by making POST requests to the following endpoint:
```
http://localhost:8000/logingestor/
```

Logs can be sent as JSON data in the request body. The server will store and make logs available for analysis.

Logs must contain valid "XUFIAGENTID" and "XUFILOGTYPE" key and value pairs for API server to accept logs.

## Configuration

You can customize the server's configuration by modifying the `database.py` file. Configure your database connection details.

## Contact

If you have any questions or need assistance, feel free to [contact me](mailto:raizn@proton.me).

---

Enjoy using XufiServer!