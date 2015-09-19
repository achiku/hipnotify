# -*- coding: utf-8 -*-
import json

import requests


class Room(object):

    """HipChat room class"""

    def __init__(self, token, room_id, debug=False, endpoint_url='https://api.hipchat.com'):
        """init Room"""
        self.token = token
        self.room_id = room_id
        self.debug = debug
        self.endpoint_url = endpoint_url
        self.notification_url = '{0}/v2/room/{1}/notification'.format(self.endpoint_url, self.room_id)
        self.headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Accept': 'application/json',
            'Content-type': 'application/json',
        }

    def notify(self, msg, color='green', notify='true', message_format='text'):
        """Send notification to specified HipChat room"""
        self.message_dict = {
            'message': msg,
            'color': color,
            'notify': notify,
            'message_format': message_format,
        }
        if not self.debug:
            return requests.post(
                self.notification_url,
                json.dumps(self.message_dict),
                headers=self.headers
            )
        else:
            print('HipChat message: <{}>'.format(msg))
            return []
