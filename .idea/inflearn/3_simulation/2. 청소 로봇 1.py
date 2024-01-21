control = {
    'R': [0,1],
    'L': [0,-1],
    'U': [-1,0],
    'D': [1,0],
}
def solution(moves):
    x = y = 0
    for s in moves:
        x += control[s][0]
        y += control[s][1]

    return [x, y]
                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
