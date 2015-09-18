# -*- coding: utf-8 -*-
from hipnotify import Room


def test_debug_room_notification(mock_hipchat):
    """Test for debug mode"""
    r = Room('test_token', '1234', debug=True)
    res = r.notify('test')
    assert res == []


def test_room_notification(mock_hipchat):
    """Test with HipChat API mock"""
    r = Room('test_token', '1234')
    res = r.notify('test')
    assert res.status_code == 200
