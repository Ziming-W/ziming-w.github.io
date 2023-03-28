<template>
    <div class="cross-nought">
      <h1>Play Cross-Nought</h1>
      <div class="board">
        <div class="row" v-for="(row, i) in board" :key="i">
          <div class="cell" v-for="(cell, j) in row" :key="j" @click="makeMove(i, j)">
            {{ cell }}
          </div>
        </div>
      </div>
      <p v-if="winner">Winner: {{ winner }}</p>
      <p v-else-if="tie">Tie game</p>
      <button @click="resetGame">Reset Game</button>
      <button @click="$router.push('/')">Go back to main page</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "CrossNought",
    data() {
      return {
        board: [
          ["", "", ""],
          ["", "", ""],
          ["", "", ""],
        ],
        currentPlayer: "X",
        winner: null,
        tie: false,
      };
    },
    methods: {
      makeMove(row, col) {
        if (!this.board[row][col]) {
          this.board[row].splice(col, 1, this.currentPlayer);
          this.currentPlayer = this.currentPlayer === "X" ? "O" : "X";
          this.checkWin();
          this.checkTie();
        }
      },
      checkWin() {
        const lines = [
          // rows
          [0, 1, 2],
          [3, 4, 5],
          [6, 7, 8],
          // columns
          [0, 3, 6],
          [1, 4, 7],
          [2, 5, 8],
          // diagonals
          [0, 4, 8],
          [2, 4, 6],
        ];
        for (let i = 0; i < lines.length; i++) {
          const [a, b, c] = lines[i];
          if (
            this.board[Math.floor(a / 3)][a % 3] &&
            this.board[Math.floor(a / 3)][a % 3] ===
              this.board[Math.floor(b / 3)][b % 3] &&
            this.board[Math.floor(a / 3)][a % 3] ===
              this.board[Math.floor(c / 3)][c % 3]
          ) {
            this.winner = this.board[Math.floor(a / 3)][a % 3];
            break;
          }
        }
      },
      checkTie() {
        const flatBoard = this.board.flat();
        if (!flatBoard.includes("") && !this.winner) {
          this.tie = true;
        }
      },
      resetGame() {
        this.board = [
          ["", "", ""],
          ["", "", ""],
          ["", "", ""],
        ];
        this.currentPlayer = "X";
        this.winner = null;
        this.tie = false;
      },
    },
  };
  </script>

<style>
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
}

.cell {
  border: 1px solid #333;
  padding: 20px;
  font-size: 40px;
  text-align: center;
}
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

h1 {
  font-size: 3rem;
  margin-bottom: 2rem;
}

.board {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 10px;
  background-color: #e1e1e1;
  padding: 10px;
  border-radius: 10px;
}

.cell {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 3rem;
  cursor: pointer;
  background-color: white;
  border-radius: 10px;
  transition: background-color 0.2s ease-in-out;
}

.cell:hover {
  background-color: #f0f0f0;
}

.player1 {
  color: #007aff;
}

.player2 {
  color: #ff2d55;
}

.turn {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.winner {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.tie {
  font-size: 2rem;
  margin-bottom: 2rem;
}
</style>