import {useContext, useEffect, useRef} from "react";
import GameContext from "../contexts/game-context.jsx";
import GameStatus from "../components/game/GameStatus.jsx";
import Card from "../components/ui/Card.jsx";
import GamePlayer from "../components/game/GamePlayer.jsx";
import GameBoard from "../components/game/GameBoard.jsx";
import GameOver from "../components/game/GameOver.jsx";
import {
    checkDraw,
    checkWinner,
    getMoveFromGPT,
    getNextTurn,
    playAudio
} from "../utils.js";
import clickSound from "../assets/click-sound.wav";
import { toast } from "react-toastify";

export default function GamePage() {
    const ctx = useContext(GameContext);

    let turn = null // Whose turn is it? X or O
    let winner = null;
    let isDraw = null;
    let isComTurn = null

    if (ctx.board) {
        turn = getNextTurn(ctx.board);
        winner = checkWinner(ctx.board);
        isDraw = !winner && checkDraw(ctx.board)
        isComTurn = !winner && !isDraw && ctx.mode === 'single' && turn === 'O';
    }

    const handleSelect = (i, j) => {
        if (ctx.settings.allowAudio) {
            playAudio(clickSound);
        }
        const newBoard = [...ctx.board];
        newBoard[i][j] = turn;
        ctx.setBoard(newBoard);
    }

    // Simulating computer's turn
    useEffect(() => {
        if (!isComTurn) return;


        getMoveFromGPT(ctx.board, ctx.settings?.difficulty).then((move) => {
            // If there is an error, show the error message
            if (move?.error) {
                toast.error(move.message);
                return;
            }

            // If the move is valid, update the board
            handleSelect(move.row, move.col);
        });

    }, [isComTurn])

    return (
        <div className='space-y-2'>
            <GameStatus />
            <Card>
                <div className="flex">
                    <GamePlayer name={ctx.settings['X']} symbol='X' isActive={turn === 'X'}/>
                    <GamePlayer name={ctx.settings['O']} symbol='O' isActive={turn === 'O'}/>
                </div>
                <GameBoard isComTurn={isComTurn} onSelect={handleSelect}/>
                {(winner || isDraw) && <GameOver winner={winner}/>}
            </Card>
        </div>
    )
}
