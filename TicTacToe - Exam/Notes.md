# Tic-Tac-Toe Game
https://en.wikipedia.org/wiki/Tic-tac-toe
## Guardians
- Initial board should be an empty (filled with 0s) 3x3 matrix :heavy_check_mark:
- Initial board negative test if not an empty matrix :heavy_check_mark:
- Initial board should be formatted as it is in the PDF file :heavy_check_mark:
- Initial board negative test, if not looks like as it is in the PDF file :heavy_check_mark:
- If there is an empty space in the board, `empty_space()` should return with an array of the x and y coordinate 
of the empty spaces :heavy_check_mark:
- If there is no empty space in the board `empty_space()` should return with an empty array :heavy_check_mark:
- Random picker test with seeded random value (makes the random value always the same) :heavy_check_mark:
- If a row is filled with the same chars the player won :heavy_check_mark:
  - Test for player 1 :heavy_check_mark:
  - Test for player 2 :heavy_check_mark:
- If no row is filled with the same chars there is no row win :heavy_check_mark:
  - Test for player 1 :heavy_check_mark:
  - Test for player 2 :heavy_check_mark:
- If a column is filled with the same chars the player won :heavy_check_mark:
  - Test for player 1 :heavy_check_mark:
  - Test for player 2 :heavy_check_mark:
- If no column is filled with the same chars there is no row win :heavy_check_mark:
  - Test for player 1 :heavy_check_mark:
  - Test for player 2 :heavy_check_mark:
## Process
1. Create the initial board :heavy_check_mark:
2. Set up the initial board :heavy_check_mark:
3. Check if there is more empty space :heavy_check_mark:
   1. If not check who won or if draw
4. Random pick for the next player :heavy_check_mark:
5. Check if the player won :small_orange_diamond:
   1. Check rows :heavy_check_mark:
   2. Check columns :heavy_check_mark:
   3. Check diagonals
6. Next player comes
7. If no winner after 9 steps the game ended with tie/draw
## DevOps
- `empty_space()` could be a list comprehension
- Change `1` and `2` inputs to `X` and `O`