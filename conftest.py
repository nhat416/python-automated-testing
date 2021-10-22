# Runtime: Python 3.8+
# Copyright:
# Project:
# Maintainer:
"""
Module Documentation:
"""
import pytest


@pytest.fixture(scope="session")
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn
