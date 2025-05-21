import pytest
import streamlit as st
from auditoria_doe.app import main

def test_hello_world(mocker):
    """Test the hello world functionality of the Streamlit app."""
    # Mock streamlit's title function
    mock_title = mocker.patch.object(st, 'title')
    
    # Call the main function
    result = main()
    
    # Assert the title was called with correct text
    mock_title.assert_called_once_with("Hello, World!")
    
    # Assert the function returns expected string
    assert result == "Hello, World!"