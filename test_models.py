import pytest
from models import Message, Author

def test_create_message():
    m = Message('A','B')
    assert m.title == 'A'
    assert m.content == 'B'

def test_create_message_with_empty_title():
    with pytest.raises(ValueError):
        m = Message('', 'B')

def test_create_message_with_long_title():
    with pytest.raises(ValueError):
        m = Message('A'*21, 'B')

def test_create_message_with_empty_content():
    with pytest.raises(ValueError):
        m = Message('A', '')

def test_create_message_with_long_content():
    with pytest.raises(ValueError):
        m = Message('A', 'B'*101)

def test_title_cannot_start_with_X():
    with pytest.raises(ValueError):
        m = Message('X', 'B')

def test_create_author():
    a = Author('A','B')
    assert a.name == 'A'
    assert a.address == 'B'

def test_assign_message_to_author():
    a = Author('A','B')
    m = Message('A','B')
    m.author_id = a.id
    assert m.author_id == a.id