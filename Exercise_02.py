from Exercise_01 import resposta
'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
resposta_dict = resposta().json()
emails = []

for user in resposta_dict["data"]:
    emails.append(user["email"])

print(emails)

