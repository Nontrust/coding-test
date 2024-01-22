control = {
    'R': [0,1],
    'L': [0,-1],
    'U': [-1,0],
    'D': [1,0],
}
def solution(n, moves):
    x = y = 0
    for s in moves:
        tx = x + control[s][0]
        ty = y + control[s][1]
        if tx in range(6) and ty in range(6):
            x=tx
            y=ty


    return [x, y]
                
                      
print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))

