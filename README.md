# User-Manager-API
# Tools & Libraries used 
- Flask with REST API
- Python
- Postman
- Vs Code

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/users`      | Get all users       |
| GET    | `/users/<id>` | Get a specific user |
| POST   | `/users`      | Add a new user      |
| PUT    | `/users/<id>` | Update a user       |
| DELETE | `/users/<id>` | Delete a user       |

| Error Message                                       | Cause                               | Fix                                             |
| --------------------------------------------------- | ----------------------------------- | ----------------------------------------------- |
| `ModuleNotFoundError: No module named 'flask'`      | Flask is not installed              | Run `pip install flask`                         |
| `app.py not recognized`                             | Trying to run `app.py` as a command | Use `python app.py` instead                     |
| `Port already in use`                               | Another app is using port 5000      | Run `app.run(port=5001)`                        |

# How to add data using Postman
# Make sure your server is running before testing in Postman.
- Click ➕ to open a new request tab
- Set Method: POST
- Enter URL: http://127.0.0.1:5000/users
  Add User Data in Request Body
- Click the Body tab
- Choose raw
- Select JSON from the dropdown
- Paste this sample data:
  -------------------------------------------------------------------------------------
   json
     {
        "name": "Dev",
        "email": "dev@example.com"
     }
  --------------------------------------------------------------------------------------
  --------------------------------------------------------------------------------------
  - Hit Send
    If successful, you'll get a response like:
---------------------------------------------------------------------------------------
json
Copy code
{
  "id": 1,
  "message": "User created successfully"
}
--------------------------------------------------------------------------------------
# Sample Output

{
  "name": "Dev",
  "email": "dev@example.com"
}

{
  "1": {
    "name": "Dev",
    "email": "dev@example.com"
  }
}

{
  "name": "Dev Updated",
  "email": "newdev@example.com"
}

{
  "message": "User 1 updated successfully"
}

----------------------------------------------------------------------------------
REFERNCE SOURCES: "GOOGLE" "CHATGPT" few Python Pdfs
----------------------------------------------------------------------------------
