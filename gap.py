# -*- coding: utf-8 -*-
import requests
import json
import mimetypes
import os


class Api:
    _base_url = 'https://api.gap.im/'
    _token = _last_message = ''

    def __init__(self, token):
        self._token = token
        if token is None:
            raise ValueError('Required "token" key not supplied')

    def get_last_message(self):
        return self._last_message

    def send_action(self, chat_id, action):
        """
        Send Action.
        :param chat_id: int
        :param action: string
        :return: Array
        """
        actions = [
            'typing'
        ]
        if action in actions:
            params = dict(chat_id=chat_id)
            return self.send_request(action, params, 'sendAction')

        raise ValueError('Invalid Action! Accepted value: '+','.join(actions))

    def send_text(self, chat_id, data, reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send text messages.
        :param chat_id: int
        :param data: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: array
        """
        params = {'chat_id': chat_id, 'data': data}
        if reply_keyboard is not None:
            params['reply_keyboard'] = json.dumps(reply_keyboard)
        if inline_keyboard is not None:
            params['inline_keyboard'] = json.dumps(inline_keyboard)
        if form is not None:
            params['form'] = json.dumps(form)

        message = self.send_request(msg_type='text', params=params, method='sendMessage')
        if message is not None:
            data = json.loads(message)
            result = data['id']
        else:
            result = False
        return result

    def send_location(self, chat_id, lat, long, desc='', reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send Location.
        :param chat_id: int
        :param lat: float
        :param long: float
        :param desc: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        data = json.dumps(dict(lat=lat, long=long, desc=desc))
        params = dict(chat_id=chat_id,data=data)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request('location', params)
        return json.loads(message)['id'] if message is not None else False

    def send_contact(self, chat_id, phone, name, reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send Contact.
        :param chat_id: int
        :param phone: string
        :param name: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        data = json.dumps(dict(phone=phone, name=name))
        params = dict(chat_id=chat_id,data=data)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request('contact', params)
        return json.loads(message)['id'] if message is not None else False

    def send_image(self, chat_id, image, desc='', reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send Image.
        :param chat_id: int
        :param image: string
        :param desc: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        msg_type = 'image'
        if json.loads(image) is None:
            if os.path.isfile(image) is None:
                raise ValueError('Image path is invalid')
            msg_type, image = self.upload_file('image', image, desc)

        params = dict(chat_id=chat_id, data=image)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request(msg_type, params)
        return json.loads(message)['id'] if message is not None else False

    def send_audio(self, chat_id, audio, desc='', reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send Audio.
        :param chat_id: int
        :param audio: string
        :param desc: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        msg_type = 'audio'
        if json.loads(audio) is None:
            if os.path.isfile(audio) is None:
                raise ValueError('Audio path is invalid')
            msg_type, audio = self.upload_file('audio', audio, desc)

        params = dict(chat_id=chat_id, data=audio)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request(msg_type, params)
        return json.loads(message)['id'] if message is not None else False

    def send_video(self, chat_id, video, desc='', reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send Video.
        :param chat_id: int
        :param video: string
        :param desc: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        msg_type = 'video'
        if json.loads(video) is None:
            if os.path.isfile(video) is None:
                raise ValueError('Video path is invalid')
            msg_type, video = self.upload_file('video', video, desc)

        params = dict(chat_id=chat_id, data=video)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request(msg_type, params)
        return json.loads(message)['id'] if message is not None else False

    def send_file(self, chat_id, file, desc='', reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send File.
        :param chat_id: int
        :param file: string
        :param desc: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        msg_type = 'file'
        if json.loads(file) is None:
            if os.path.isfile(file) is None:
                raise ValueError('File path is invalid')
            msg_type, file = self.upload_file('file', file, desc)

        params = dict(chat_id=chat_id, data=file)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request(msg_type, params)
        return json.loads(message)['id'] if message is not None else False

    def send_voice(self, chat_id, voice, desc='', reply_keyboard=None, inline_keyboard=None, form=None):
        """
        Send Voice.
        :param chat_id: int
        :param voice: string
        :param desc: string
        :param reply_keyboard: string
        :param inline_keyboard: array
        :param form: json
        :return: Array
        """
        msg_type = 'voice'
        if json.loads(voice) is None:
            if os.path.isfile(voice) is None:
                raise ValueError('Voice path is invalid')
            msg_type, voice = self.upload_file('voice', voice, desc)

        params = dict(chat_id=chat_id, data=voice)
        if reply_keyboard is not None:
            params.update({'reply_keyboard': reply_keyboard})
        if inline_keyboard is not None:
            params.update({'inline_keyboard': inline_keyboard})
        if form is not None:
            params.update({'form': form})

        message = self.send_request(msg_type, params)
        return json.loads(message)['id'] if message is not None else False

    def edit_message(self, chat_id, message_id, data=None, inline_keyboard=None):
        """
        Edit Message.
        :param chat_id: int
        :param message_id: int
        :param data: string
        :param inline_keyboard: array
        :return: array
        """
        params = dict(chat_id=chat_id, message_id=message_id, inline_keyboard=inline_keyboard)
        if inline_keyboard is not None:
            if isinstance(inline_keyboard, list) is False:
                raise ValueError('Inline keyboard is invalid')
            params.update({'inline_keyboard': json.dumps(inline_keyboard)})
        return self.send_request(None, params, 'editMessage')

    def delete_message(self, chat_id, message_id):
        """
        Delete Message.
        :param chat_id: int
        :param message_id: int
        :return: array
        """
        params = dict(chat_id=chat_id, message_id=message_id)
        return self.send_request(None, params, 'deleteMessage')

    def answer_callback(self, chat_id, callback_id, text, show_alert=False):
        """
        Answer Callback.
        :param chat_id: int
        :param callback_id: int
        :param text: string
        :param show_alert: boolean
        :return: array
        """
        params = {'chat_id': chat_id, 'callback_id': callback_id, 'text': text}
        if show_alert:
            params['show_alert'] = 'true'
        else:
            params['show_alert'] = 'false'
        return self.send_request(None, params, 'answerCallback')

    def send_invoice(self, chat_id, amount, description):
        """
        Send Invoice
        :param chat_id: int
        :param amount: int
        :param description: string
        :return: string
        """
        params = dict(chat_id=chat_id, amount=amount, description=description)
        result = self.send_request(None, params, 'invoice')
        result = json.loads(result)
        return result['id']

    def pay_verify(self, chat_id, ref_id):
        """
        Pay verify
        :param chat_id: int
        :param ref_id: int
        :return: boolean
        """
        params = dict(chat_id=chat_id, ref_id=ref_id)
        result = self.send_request(None, params, 'payVerify')
        result = json.loads(result)
        if isinstance(result, list) is True:
            return result['status'] == 'verified'

    def pay_inquiry(self, chat_id, ref_id):
        """
        Pay inquiry.
        :param chat_id: int
        :param ref_id: int
        :return: boolean
        """
        params = dict(chat_id=chat_id, ref_id=ref_id)
        result = self.send_request(None, params, 'payInquiry')
        result = json.loads(result)
        if isinstance(result, list) is True:
            return result['status'] == 'verified'

    def request_wallet_charge(self, chat_id, desc=None):
        params = dict(chat_id=chat_id, desc=desc)
        return self.send_request(None, params, 'requestWalletCharge')

    def reply_keyboard(self, keyboard, once=True, selective=False):
        """
        Reply keyboard.
        :param keyboard: keyboard
        :param once: once
        :param selective: boolean
        :return: boolean
        """
        if isinstance(keyboard, list) is True:
            raise ValueError("Keyboard must be array")
        reply_keyboard = dict(keyboard=keyboard, once=once, selective=selective)
        return json.dumps(reply_keyboard)

    def send_request(self, msg_type, params, method='sendMessage'):
        if msg_type is not None:
            params['type'] = msg_type

        if method == 'sendMessage':
            self._last_message = params

        headers = {'token': self._token}
        url = self._base_url+method
        r = requests.post(url=url, data=params, headers=headers)
        if r.status_code != 200:
            if r is not None:
                raise ValueError(r.text)
            raise ValueError('An error was encountered.')

        return r.text






