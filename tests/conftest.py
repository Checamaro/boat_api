import pytest
from src.models.rowboat import Rowboat

@pytest.fixture
def boat():
    return Rowboat(capacity=2)
