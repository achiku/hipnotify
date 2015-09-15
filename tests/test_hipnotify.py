# -*- coding: utf-8 -*-
from hipnotify import Room


def test_room_notification():
    """Easy test which doesn't have much meaning"""
    r = Room('test_token', 'test_room_id', debug=True)
    r.notify('test')
