# insp
Python project where people call in and get to hear an inspirational message built on Africa's Talking Voice API.

### About

Sample voice dating application with AfricasTalking API's.


### Install

```bash
pip install -r requirements.txt
```


### run

```bash
python runserver.py


### Logic. More detailed Readme, I guess.

Using SMS that alerts the user to register using a similar SMS format like what Ian demoed.
When the user call in then you serve them content.

The idea is to serve people with content in terms of inspirational messages i.e user calls in and they get to hear an inspirational audio message.

So what had earlier, but now with sms registration factored in.

1. User gets text asking to register, if they want to get inspirational messages! The text will only take from them their name. This will be so that they can get personalized calls.
The text will read: "Welcome to this service. To register text your name and gender to 20880 starting with the word Inspire e.g Inspire Walter*27*Male"

2. User sends the text message. On sending, they receive confirmation text "Thank you for registering for this service. To get inspirational messages, call 20880. Calls charged at 10 bob per minute. Have a blessed day."

3. User calls the number. Met with the message:
"Welcome, xxxxx....... For inspirational messages on how to overcome procrastrination, Press 1, For messages on self-improvement, press 2, For messages"

4. User enters key as prompted.

5. Based on key entered, an audio message is played. The message is an audio file stored in the server. The messages are stored to be played in a random manner. If user has called in before, messages played to him are not to be replayed, until all available messages in a particular category have been played. Then they can be replayed.

Q: Can it be possible for an audio message to be marked or favorited so the user can retrieve it and have it played over and over at will?

6. After message is played, user is again prompted for input as "For another message, press 9. To go back to the main menu, press 1."

7. If no user interaction within 10 seconds, call auto-terminates with message "thanks for calling, have a fruitful day Mr. x"

The average call would not last more than two minutes.
