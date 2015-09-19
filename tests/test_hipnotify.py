# -*- coding: utf-8 -*-
from hipnotify import Room


def test_debug_room_notification(mock_hipchat):
    """Test for debug mode"""
    hip = Room('test_token', '1234', debug=True)
    res = hip.notify('test')
    assert res == []


def test_room_notification(mock_hipchat):
    """Test with HipChat API mock"""
    hip = Room('test_token', '1234')
    res = hip.notify('test')
    assert res.status_code == 200
