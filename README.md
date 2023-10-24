# fast-api-sample-app

Sample web app using Python FastAPI framework.
The app has 3 interations:
- Accessing the root path (http://localhost:5000/) to display a simple HTML page with an image and a text;
- Accessing the root path with a variable (http://localhost:5000/MyName) to display the same home page but with a twist;
- Accessing a different path (http://localhost:5000/home) to display a message.

In order to run the application, you must execute the following commands. Make sure to have Python installed in your computer.

Make sure you have Pipenv installed in you computer by running:

```
pip install pipenv
```

Firstly, we will install all the necessary dependencies in the virtual environment of Pipenv. 

```
pipenv install
```

By doing this, we are installing all necessary Python libraries, including the framework itself along with others.

Activate the virtual environment in order to have access to all these libraries:

```
pipenv shell
```

All is set to run the application:

```
uvicorn main:app --host 0.0.0.0 --port 5000
```

Now go to your browser of choice and access ```http://localhost:5000```
