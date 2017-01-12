#!/usr/bin/env pyhton3
# -*- coding: utf-8 -*-

'''
url handlers
'''

import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    summary = 'asdfnk oipo sadohf oiuhsakdj oiuhykjsad fiuhykjbsad hujasdf joiuads jfsadf uasdok qoweihj f sadi qjwkefds foiajf da.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='FOOBAR', summary=summary, created_at=time.time()-3500),
        Blog(id='3', name='BLABLA', summary=summary, created_at=time.time()-7200),
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
