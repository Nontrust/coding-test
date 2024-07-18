dx = [1,-1,0,0]
dy = [0,0,1,-1]
def solution(board):
    answer = 0
    for x in range(5):
        for y in range(5):
            if board[x][y]  == 1:
                answer += 1
                DFS(x,y,board)

    
    return answer

def DFS(x, y, board):
    board[x][y] =0
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if(nx >= 0 and nx <5 and ny >= 0 and ny < 5 and board[nx][ny]):
            DFS(nx,ny,board)


            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

