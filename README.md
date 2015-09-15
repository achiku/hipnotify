# hipnotify

[![PyPI version](https://img.shields.io/pypi/v/hipnotify.svg)](https://pypi.python.org/pypi/hipnotify)
[![PyPI downloads](https://img.shields.io/pypi/dm/hipnotify.svg)](https://pypi.python.org/pypi/hipnotify)
[![Build Status](https://travis-ci.org/achiku/hipnotify.svg)](https://travis-ci.org/achiku/hipnotify)
[![Dependency Status](https://gemnasium.com/achiku/hipnotify.svg)](https://gemnasium.com/achiku/hipnotify)


Deadly simple HipChat API V2 room notification library


# Why created

I wanted HipChat V2 API + Python3 compatible HipChat client which can only send messages to the specified room.


# Usage

```
# -*- coding: utf-8 -*-
from hipnotify import Room

HIPCHAT_TOKEN = 'token'
HIPCHAT_ROOM_ID = 'room_id'


if __name__ == '__main__':
    room = Room(HIPCHAT_TOKEN, HIPCHAT_ROOM_ID)
    room.notify('hello, world!')
```
