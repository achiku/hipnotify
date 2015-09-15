# hipnotify

[![PyPI version](https://img.shields.io/pypi/v/hipnotify.svg)](https://pypi.python.org/pypi/hipnotify)
[![PyPI downloads](https://img.shields.io/pypi/dm/hipnotify.svg)](https://pypi.python.org/pypi/hipnotify)
[![Build Status](https://travis-ci.org/achiku/hipnotify.svg)](https://travis-ci.org/achiku/hipnotify)
[![Dependency Status](https://gemnasium.com/achiku/hipnotify.svg)](https://gemnasium.com/achiku/hipnotify)


Deadly simple HipChat API V2 room notification library


# Why created

HipChat official [third-party library web page](https://www.hipchat.com/docs/apiv2/libraries) introduces two sophisticated Python client libraries supporting almost all V2 APIs currently available. However, our usecase just needed HipChat V2 room notification API + Python3 compatible HipChat client, which can only send messages to the specified room if a room token is given, without needing an admin token. (Admin token could be pretty dangerous and certainly unnecessary in this case.)

This library is designed to do simple thing simple with minimum sysadmin concern.


# Usage

```python
# -*- coding: utf-8 -*-
from hipnotify import Room

HIPCHAT_TOKEN = 'token'
HIPCHAT_ROOM_ID = 'room_id'


if __name__ == '__main__':
    room = Room(HIPCHAT_TOKEN, HIPCHAT_ROOM_ID)
    room.notify('hello, world!')
```

![](artwork/green-hello-world.png)


```python
room.notify('Watch out!! Something is going wrong!!', color='red')
```

![](artwork/red-caution.png)


```python
room.notify('Ha? Just <a href="https://google.com">google</a> it.', message_format='html')
```

![](artwork/green-html-format.png)
