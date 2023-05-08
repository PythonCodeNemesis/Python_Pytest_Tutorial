import pytest

@pytest.fixture
def sample_data():
    # This fixture returns a dictionary with some sample data
    return {
        'name': 'John',
        'age': 30,
        'email': 'john@example.com'
    }

def test_name(sample_data):
    assert sample_data['name'] == 'John'

def test_age(sample_data):
    assert sample_data['age'] == 30

def test_email(sample_data):
    assert sample_data['email'] == 'john@example.com'
