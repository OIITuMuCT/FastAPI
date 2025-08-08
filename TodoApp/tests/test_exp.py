""" Pytest Basic """

def test_equal_or_not_equal():
    """# Test Validate Integers"""
    assert 3 == 3

def test_is_instance():
    """ # Test Validate Instances """
    assert isinstance('this is a string', str)
    assert not isinstance('10', int)

def test_boolean():
    """ Test Validate Boolean """
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False

def test_type():
    """# Test Validate Types """
    assert type('Hello' is str)
    assert type('World' is not int)

def test_greater_and_than():
    """# Test Validate Greater Than & Less Than  """
    assert 7 > 3
    assert 4 < 10

def test_list():
    """ Validate Types """
    num_list = [1, 2,3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)
