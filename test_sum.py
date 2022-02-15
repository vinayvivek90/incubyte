import pytest
from sum import Add

def test_empty():
	assert Add("") == 0

def test_one():
	assert Add("1") == 1

def test_two_values():
	assert Add("1,2") == 3

def test_newline():
	assert Add("1\n2,3") == 6

def test_multiple_delimiter():
	assert Add("1,\n") == 'bad input'

def test_delimiter():
	assert Add('//;\n1;2') == 3