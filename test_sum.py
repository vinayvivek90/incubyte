import pytest
from sum import Add

def test_empty():
	assert Add("") == 0

def test_one():
	assert Add("1") == 1

def test_two_values():
	assert Add("1,2") == 3