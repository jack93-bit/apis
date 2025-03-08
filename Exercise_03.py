'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

dados = {"email":"jk@gmail.com",
        "first_name":"Jacqueline",
        "last_name": "Alves"}

requests.post(base_url, json=dados)

resposta = requests.get(base_url)
print(resposta.text)