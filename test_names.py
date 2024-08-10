from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Test the make full name function """

    assert make_full_name("Sam", "Smith") == "Smith; Sam"

def test_extract_family_name():
    """Test extract family name function"""

    assert extract_family_name("Sam", "Smith") == "Smith"

def test_extract_given_name():
    

    assert extract_given_name("Sam", "Smith") == "Sam"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
