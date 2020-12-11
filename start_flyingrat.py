#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import subprocess
import tempfile
import shutil
import smtplib
import time

python_libs_dir = "python_libs"

mail_dir = tempfile.mkdtemp("flyingrat")
flyingrat = subprocess.Popen([
    "python",
    "-m", "flyingrat.cli",
    mail_dir,
], env={"PYTHONPATH": python_libs_dir})

time.sleep(2)

smtp = smtplib.SMTP('localhost:5050')

with open("test.eml", 'r') as f:
    msg_text = f.read()
smtp.sendmail("test@test.de", "test@test.de", msg_text)
