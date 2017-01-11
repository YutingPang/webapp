<<<<<<< HEAD
#!/usr/bin/env python3
=======
#!/usr/bin/env pyhton3
>>>>>>> 90218e27d60363c308d3845106509d5782bf7926
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
<<<<<<< HEAD
import asycio
from coroweb import get, post
from models import User, Comment, Blogs, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'user': users
=======
import asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    return {
        '__template__': 'test.html',
        'users': users
>>>>>>> 90218e27d60363c308d3845106509d5782bf7926
    }
