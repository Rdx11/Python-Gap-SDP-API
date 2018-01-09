# Python-Gap-SDP-API
⚡ A Python class for the Gap Messenger SDP API.

### What is Gap?
According to [Gap Messenger](https://gap.im/):

Gap is a messaging app with a focus on speed and security, it’s super fast, simple and free. You can use Gap on all your devices at the same time — your messages sync seamlessly across any of your phones, tablets or computers.

With Gap, you can send text, photos, videos and files of any type (doc, zip, mp3, etc), as well as create groups for up to 200 people. You can write to your phone contacts and find people by their usernames. As a result, Gap is like SMS and email combined — and can take care of all your personal or business messaging needs.


## Usage example:

### Send text message:
```python
chat_id = 9854756
Api.send_text(
    chat_id,
    data='Selec reminder type',
    reply_keyboard={
          'keyboard': [
              [{'/Cancel': 'Cancel'}]
          ],
          'once': True,
          'selective': False
    },
    inline_keyboard=[
          [
              {'cb_data': '/Meeting', 'text': 'Metting'},
              {'cb_data': '/Session', 'text': 'Session'},
              {'cb_data': '/Buying', 'text': 'Buying'}
          ],
          [
              {'cb_data': '/Ceremony', 'text': 'Ceremony'},
              {'cb_data': '/Party', 'text': 'Party'},
              {'cb_data': '/Congratulate', 'text': 'Congratulate'},
          ]
    ]
)
```