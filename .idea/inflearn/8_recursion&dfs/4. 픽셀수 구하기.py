mx = [1,0,-1,0]
my = [0,1,0,-1]
cnt = 0

def solution(board):
    global cnt
    answer = []
    for x in range(5):
        for y in range(5):
            if board[x][y] == 1:
                cnt = 0
                DFS(x, y, board)
                answer.append(cnt)
    return answer

def DFS(x,y,board):
    global cnt
    board[x][y] = 0
    cnt = cnt + 1
    for k in range(4):
        dx = mx[k] + x
        dy = my[k] + y
        if dx>=0 and dy>=0 and dx<5 and dy<5 and board[dx][dy] == 1:
            DFS(dx,dy,board)
# 5,3
# 7,


print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

