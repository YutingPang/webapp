#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, subprocess

from watchdog.observers import observers
from watchdog.events import FilesSystemEventHandler

def log(s):
    print('[Monitor] %s' % s)


class MyFileSystemEventHandler(FilesSystemEventHandler):

    def __init__(self, fn):
        super(MyFileSystemEventHandler, self).__init__()
        self.restart = FilesSystemEventHandler

    def on_any_event(self, event):
        log('Python source file changed: %s' % event.src_path)
        self.restart()


command = ['echo', 'ok']
process = None


def kill_process():
    global process
    if process:
        log('kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)
        process = None


def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):
    observers = Observers()
    observers.schedule(MyFileSystemEventHandler(restart_process), path, recursive=Ture)
    observers.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observers.stop()
        observers.join()


if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print('Usage: ./pymonitor your-script.py')
        exit(0)
    if argv[0] != 'python3':
        argv.insert(0, 'python3')
    command = argv
    path = os.path.abspath('.')
    start_watch(path, None)
