import streamlit as st
import numpy as np

# Initialize the game board (3x3 grid)
if 'board' not in st.session_state:
    st.session_state.board = np.full((3, 3), '', dtype=str)

if 'player' not in st.session_state:
    st.session_state.player = 'X'

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] and board[i, 0] != '':
            return board[i, 0]
        if board[0, i] == board[1, i] == board[2, i] and board[0, i] != '':
            return board[0, i]
    
    if board[0, 0] == board[1, 1] == board[2, 2] and board[0, 0] != '':
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] and board[0, 2] != '':
        return board[0, 2]

    if '' not in board:
        return 'Tie'
    
    return None

def reset_game():
    st.session_state.board = np.full((3, 3), '', dtype=str)
    st.session_state.player = 'X'

st.title('Tic-Tac-Toe Game')

# Display the current player
st.write(f"Current Player: {st.session_state.player}")

# Create buttons for each cell in the 3x3 grid
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        if cols[col].button(st.session_state.board[row, col] or ' ', key=f'{row}-{col}'):
            if st.session_state.board[row, col] == '':
                st.session_state.board[row, col] = st.session_state.player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.write(f"Player {winner} wins!" if winner != 'Tie' else "It's a Tie!")
                    if st.button('Restart Game'):
                        reset_game()
                else:
                    # Switch the player
                    st.session_state.player = 'O' if st.session_state.player == 'X' else 'X'

# Show the board as text (optional)
st.write(st.session_state.board)
