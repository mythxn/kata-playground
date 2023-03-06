import os

import pytest
from dotenv import load_dotenv
from pytest import MonkeyPatch

from app.main import *

load_dotenv()

SUPER_SECRET_KEY = os.getenv('SUPER_SECRET_KEY')


def test_hello_world():
    assert hello_world() == 'Hello World!'


def test_super_secret_key():
    assert SUPER_SECRET_KEY == 'super-secret-key'
