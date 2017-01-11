#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
url handlers
'''

import re
import time
import json
import logging
import hashlib
import base64
import asycio
from coroweb import get, post
from models import User, Comment, Blogs, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'user': users
    }
