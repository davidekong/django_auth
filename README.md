# django_auth!
Once this repository is cloned on your system using the terminal, enter it's directory using this:
```
cd django_auth
```
and run the following commands
```
python manage.py runserver
```

make sure to type in the url address in your browser:
```
http://127.0.0.1:8000/register/
```

This is a simple snippet of code that uses the built in django authentication to bring the register, login and logout services to the user.

This is a simple video showing the features of this web app.
https://user-images.githubusercontent.com/66387173/195411716-1723bab1-15b8-4459-90c1-38962b855e9a.mp4


Here, we register a new user using the credentials as follows;
![register](https://user-images.githubusercontent.com/66387173/195412059-e6e3085b-43f5-449e-bf42-8f7bf32dca95.png)

Here, we can authenticate a user with already an already existing account
![login](https://user-images.githubusercontent.com/66387173/195412108-d5e956f4-e4bc-442e-9a7e-ab83225556d9.png)

This is the success result if user is authenticated (Dashboard), containing the users username, email and a logout button.
![dashboard](https://user-images.githubusercontent.com/66387173/195412082-125f5da0-8a0f-4998-9ce3-e9a00bda2f69.png)

If the user has forgotten the password associated with his/her account, he/she can retrive it by filling in the email that he/she used to register.
![forget password](https://user-images.githubusercontent.com/66387173/195412097-928050d0-d87d-459a-a895-3650a57cc5da.png)

A link will be sent to the users email which will enable him/her to change their password.
![email sent](https://user-images.githubusercontent.com/66387173/195412092-0a9f418e-f2f8-4bba-a757-82eb99ec9905.png)

This is the password changing page.
![change password](https://user-images.githubusercontent.com/66387173/195412075-6db0e95a-0438-4360-ae76-bebef3a8f22c.png)

Created by David Ekong.
