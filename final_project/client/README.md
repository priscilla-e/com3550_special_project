# TIC-TAC-TOE Web Client

# Tic-Tac-Toe React Application

This is a modern, interactive Tic-Tac-Toe game built with React. The application features both single-player mode with AI opponent and multiplayer mode for playing with friends.

## Features

- **Game Modes**: Choose between single-player (vs AI) and multiplayer modes
- **Customizable Players**: Set custom names for players
- **Difficulty Levels**: In single-player mode, select AI difficulty (easy, medium, hard)
- **Responsive Design**: Optimized for both desktop and mobile devices
- **Sound Effects**: Audio feedback for game actions (can be toggled on/off)
- **Game Statistics**: Track wins, losses, and draws


## Run the application Locally

1. Navigate to the client directory
```
cd client
```

2. Install node dependencies
```
npm install
```

3. Start the development server
```
npm run dev
```

4. Open your browser and visit `http://localhost:5173`

NOTE: Ensure the server is running before opening the client.


## Project Structure

```
client/
├── public/
│   ├── favicon.ico                  # App favicon
│   ├── index.html                   # HTML entry point
│   └── logo.png                     # App logo for browser tab
├── src/
│   ├── assets/
│   │   ├── sounds/
│   │   │   ├── click.mp3            # Sound effect for moves
│   │   │   ├── win.mp3              # Sound effect for winning
│   │   │   └── draw.mp3             # Sound effect for draw games
│   │   └── images/
│   │       └── logo.svg             # App logo SVG
│   ├── components/
│   │   ├── Board/
│   │   │   ├── Board.jsx            # Game board component (3x3 grid)
│   │   │   └── Board.css            # Board-specific styles
│   │   ├── Square/
│   │   │   ├── Square.jsx           # Individual square component
│   │   │   └── Square.css           # Square-specific styles
│   │   ├── GameStatus/
│   │   │   ├── GameStatus.jsx       # Shows current player and game status
│   │   │   └── GameStatus.css       # Status-specific styles
│   │   ├── GameOver/
│   │   │   ├── GameOver.jsx         # Modal shown when game ends
│   │   │   └── GameOver.css         # Modal-specific styles
│   │   ├── PlayerInfo/
│   │   │   ├── PlayerInfo.jsx       # Shows player information (X/O)
│   │   │   └── PlayerInfo.css       # Player info styles
│   │   ├── Settings/
│   │   │   ├── Settings.jsx         # Settings form components
│   │   │   └── Settings.css         # Settings-specific styles
│   │   └── ModeSelector/
│   │       ├── ModeSelector.jsx     # Game mode selection buttons
│   │       └── ModeSelector.css     # Mode selector styles
│   ├── context/
│   │   └── GameContext.jsx          # Game state context provider
│   ├── pages/
│   │   ├── Game/
│   │   │   ├── Game.jsx             # Main game page component
│   │   │   └── Game.css             # Game page styles
│   │   ├── Home/
│   │   │   ├── Home.jsx             # Landing page with mode selection
│   │   │   └── Home.css             # Home page styles
│   │   └── Settings/
│   │       ├── Settings.jsx         # Game configuration page
│   │       └── Settings.css         # Settings page styles
│   ├── utils/
│   │   ├── gameLogic.js             # Game logic (win checking, valid moves)
│   │   └── aiPlayer.js              # AI opponent logic for different difficulties
│   ├── App.jsx                      # Main app component with routing
│   ├── App.css                      # Global app styles
│   ├── index.jsx                    # React entry point
│   └── index.css                    # Global CSS reset and variables
├── package.json                     # Project dependencies and scripts
├── README.md                        # Project documentation
└── .gitignore                       # Git ignore configuration
```