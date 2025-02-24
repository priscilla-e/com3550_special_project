import {useContext, useEffect, useState} from "react";
import Card from "../components/ui/Card.jsx";
import Button from "../components/ui/Button.jsx";
import GameContext from "../contexts/game-context.jsx";
import {createEmptyGameBoard} from "../utils.js";
import { HiOutlineSelector } from "react-icons/hi";

export default function SettingsPage() {
  const ctx = useContext(GameContext);

  const [player1, setPlayer1] = useState("");
  const [player2, setPlayer2] = useState("COM");
  const [difficulty, setDifficulty] = useState("easy");
  const [error, setError] = useState(null);


  useEffect(() => {
    // Reset error message when player1 or player2 changes
    setError(null);
  }, [player1, player2]);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!player1.trim()) {
      setError("Player 1 name is required.");
      return;
    }

    if (!player2.trim()) {
      setError("Player 2 name is required.");
      return;
    }

    const settings = {
      X: player1.toUpperCase(),
      O: player2.toUpperCase(),
      difficulty, // Used only in single player mode
      allowAudio: true,
    };

    // Save game settings and start game
    ctx.setSettings(settings);
    ctx.setBoard(createEmptyGameBoard(3)); // set game board
    ctx.setPage((curPage) => curPage + 1); // go to game page
  };

  const handleBack = () => {
    ctx.setPage((curPage) => curPage - 1);
    ctx.setMode(null);
  };

  return (
    <Card title="Select Settings">
      <p className="my-2 text-center text-xs text-red-800">{error}</p>
      <form className="max-w-xs mx-auto mt-4 md:mt-8" onSubmit={handleSubmit}>
        <div className="flex items-center justify-between space-y-2">
          <label htmlFor="player1" className="mr-5">
            Player 1
          </label>
          <input
            value={player1}
            type="text"
            name="player1"
            id="player1"
            placeholder="name"
            className="appearance-none w-8/12 px-2 py-4 text-sm text-smoke uppercase bg-darkEarth md:p-4 focus:outline-none"
            onChange={(e) => setPlayer1(e.target.value)}
          />
        </div>
        {ctx.mode === "multi" && (
          <div className="flex items-center justify-between space-y-2">
            <label htmlFor="player2">Player2</label>
            <input
              value={player2}
              type="text"
              name="player2"
              id="player2"
              placeholder="name"
              className="appearance-none w-8/12 px-2 py-4 text-sm text-smoke uppercase bg-darkEarth md:p-4 focus:outline-none"
              onChange={(e) => setPlayer2(e.target.value)}
            />
          </div>
        )}

        {ctx.mode === "single" && (
          <div className="flex items-center justify-between space-y-2">
            <label htmlFor="difficulty">Difficulty</label>
            <div className="relative w-8/12">
              <select
                id="difficulty"
                name="difficulty"
                value={difficulty}
                className="appearance-none w-full block px-2 py-4 text-sm text-smoke uppercase bg-darkEarth md:p-4 focus:outline-none"
                onChange={(e) => setDifficulty(e.target.value)}
              >
                <option value="easy">Easy - GPT 3.5</option>
                <option value="medium">Medium - GPT 4</option>
                <option value="hard">Hard - GPT 4o</option>
              </select>
              <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2">
                <HiOutlineSelector />
              </div>
            </div>
          </div>
        )}

        <div className="mt-10 flex justify-between p-0">
          <Button type="button" onClick={handleBack}>
            Back
          </Button>
          <Button type="submit">Start Game</Button>
        </div>
      </form>
    </Card>
  );
}