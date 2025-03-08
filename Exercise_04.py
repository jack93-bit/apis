'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users/10470"
dados = {"email":"jkas@gmail.com", 
         "first_name":"Jacqueline",
         "last_name":"Silva"}

requests.put(base_url, json=dados)

pprint(requests.get(base_url).json())