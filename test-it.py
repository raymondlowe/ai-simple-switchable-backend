import os
from simpleai import SimpleAI
from simpleai import AIBackEndType as BackEnd

def test_simple_ai():
    """Test creating a SimpleAI instance"""

    # Get the access token from an environment variable
    access_token = os.environ.get('OpenAIKey')

    # Initialize the SimpleAI class with a backend and access token
    ai = SimpleAI(BackEnd.OpenAI, access_token)

    # Make sure the backend and access token were set correctly
    assert ai.backEnd == BackEnd.OpenAI
    assert ai.AccessToken == access_token
