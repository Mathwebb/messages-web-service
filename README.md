# messages-web-service
Small Resftull web application made as a practical work in the distributed systems class. The objective was to avoid the use of frameworks that improve the level of abstraction, instead several low level libraries were used to develop this project.

## API endpoints (English)
The backend API that allows integration with the frontend uses JSON files for communication and has the following endpoints that follow these formats:

- GET
  - /message - returns all messages that have been sent in the system, regardless of who sent or received them;
  - /message?message_id=4 - returns the message that has the id equal to 4 or returns an error if there is no message with that id;
  - /message?sender_email=example@example.com - returns messages sent by a specific user with the email address provided, in this case example@example.com;
  - /message?recipient_email=example@example.com - returns all messages received by a specific user with the email address provided, in this case example@example.com;
  - /user - returns all users registered in the system;
  - /user?user_id=3 - returns the user whose id is equal to the id provided in the request;
  - /user?email_address=example@example.com - returns the user whose email address is equal to the email address provided in the request;
- POST
  - /user - registers a new user in the system, the request body must be a JSON in the following format:

        {
        "name": "username",
        "email_address": "example@example.com"
        }
  - /message - sends a new message to some user in the system, the request body must be a JSON in the following format:

        {
          "sender_email": 'sender@email.com",
          "recipient_email": 'recipient@email.com",
          "subject": "Meeting at the park",
          "body": "I went to the park yesterday, did not find you there."
        }

- DELETE
  - /message?message_id=2 - deletes one of the messages that have been sent whose id is equal to the id provided in the request;
  - /user?user_id=3 - deletes a user from the system whose id is equal to the id provided in the request;

## How to use
To use the application you need to clone the github repository using the following command:

```
git clone https://github.com/Mathwebb/messages-web-service.git
```

The application uses the following libraries, all of the following libraries are included in the default python library, so there's no need to install any of the libraries:
- http.server
- json
- sqlite3

To be able to execute the application you need to have python in version 3.10.6 or above, also it's necessary to use the following command in the project's root directory to start the http server:
- python3 src/server.py (Linux)
- python src/server.py (Windows)

After starting the server you can proceed to use the application by opening your browser and going to http://localhost:8000/login. I tested the application on firefox and opera GX, but should work in any other browser of your liking.
