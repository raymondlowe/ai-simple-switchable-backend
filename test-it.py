import os
from simpleai.simpleai import SimpleAI
from simpleai.simpleai import AIBackEndType as BackEnd

def test_simple_ai_with_openai():
    """Test creating a SimpleAI instance and getting a reply from the AI"""

    # Get the access token from an environment variable
    access_token = os.environ.get('OpenAIKey')

    # Initialize the SimpleAI class with a backend and access token
    ai = SimpleAI(BackEnd.OpenAI, access_token)

    # Make sure the backend and access token were set correctly
    assert ai.backEnd == BackEnd.OpenAI
    assert ai.AccessToken == access_token

    # Test getting a response from the AI
    response = ai.reply("hello")
    assert isinstance(response, str)
    print(response)


def test_simple_ai_with_poe():
    """Test creating a SimpleAI instance and getting a reply from the AI"""

    # Get the access token from an environment variable
    access_token = os.environ.get('poekey')

    # Initialize the SimpleAI class with a backend and access token
    ai = SimpleAI(BackEnd.Poe, access_token)

    # Make sure the backend and access token were set correctly
    assert ai.backEnd == BackEnd.Poe
    assert ai.AccessToken == access_token

    # Test getting a response from the AI
    response = ai.reply("hello")
    assert isinstance(response, str)
    print(response)


test_simple_ai_with_poe()