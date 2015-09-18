# -*- coding: utf-8 -*-
import re

import httpretty
import pytest


@pytest.yield_fixture(scope='function')
def mock_hipchat():
    """Mock for HipChat room notification API"""
    httpretty.enable()
    httpretty.register_uri(
        httpretty.POST,
        re.compile('https://api.hipchat.com/v2/room/(\d+)/notification'),
        status=200,
    )
    yield httpretty
    httpretty.disable()
