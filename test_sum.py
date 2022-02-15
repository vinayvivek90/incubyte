import pytest
from sum import sum

def test_empty():
	assert sum("") == 0

def test_one():
	assert sum('1') == 1