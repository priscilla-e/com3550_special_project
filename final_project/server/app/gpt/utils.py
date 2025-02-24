"""
Helper functions for the API.
"""


def get_model(difficulty: str) -> str:
    """
    Get the model based on selected difficulty.

    Note:
        - Not all models support JSON mode.
        - More info: https://platform.openai.com/docs/guides/structured-outputs#json-mode

    :param difficulty: game difficulty (east, medium, hard)
    :return: model name as a string
    """
    model = "gpt-3.5-turbo"

    if difficulty == "medium":
        model = "gpt-4-turbo"
    elif difficulty == "hard":
        model = "gpt-4o"

    return model