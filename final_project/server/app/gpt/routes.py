from flask import request
from app.gpt import gpt_bp
from app.extensions import client
from app.gpt.utils import get_model

# GET: '/api/gpt'
@gpt_bp.route('/gpt', methods=['GET'])
def home():
    return {
        "msg": "API is working!",
        "resource": "gpt",
        "endpoints": {
            "gpt_move": {
                "url": "/api/gpt/move",
                "methods": ["POST", "GET"],
                "description": "Use the GPT engine to generate a move for the AI player."
            }
        }
    }


# POST, GET: '/api/gpt/move'
@gpt_bp.route("/gpt/move", methods=["GET", "POST"])
def gpt_move():
    """
    Use the GPT engine to generate a move for the AI player.
    :return: The move as a JSON object {row: int, col: int}
    """

    # Get the data from the request
    data = request.get_json()
    board = data.get('board')
    difficulty = data.get('difficulty')

    # Data validation: Verify that the board is provided
    if not board:
        return {"msg": "Board is required."}, 400

    # Get the model based on the difficulty
    model = get_model(difficulty)

    # Send a request to the GPT engine to get AI move
    response = client.chat.completions.create(
        model=model,
        temperature=0.9,
        response_format={"type": "json_object"},
        max_tokens=150,
        messages=[
            {"role": "system",
             "content": f"You are an opponent in a 3x3 Tic-Tac-Toe game. You're playing as 'O' and your goal is to win. Suggest the indexes of the next move as 'row,col' in JSON format. Do not suggest cells that are already occupied."},
            {"role": "user",
             "content": f"Given the current Tic-Tac-Toe board:\n{board}\nMake the next move for 'O':"},
        ],
    )

    # Get the move from the response
    move = response.choices[0].message.content

    # Return the move to the client
    return move