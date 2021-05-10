import pytest

@pytest.fixture
def repo_test_data():
    return { 
            "name": "Test name",
            "description": "Test desc",
            "language": "Test lanf"
    }


@pytest.fixture()
def repo_test_list():
    return [
        { 
            "name": "Test name",
            "description": "Test desc",
            "language": "Test lanf"
        },
        { 
            "name": "Test name2",
            "description": "Test desc2",
            "language": "Test lang2"
        }
    ]