import pytest
from sum import sum

def test_empty():
	assert sum("") == 0