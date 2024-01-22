control = [[1,0],[0,1],[-1,0],[0,-1]]
def solution(moves):
    x = y = 0
    focus = 0
    for mov in moves:
        if mov == 'G':
            x += control[focus][1]
            y += control[focus][0]
        elif mov =='R':
            focus = (focus+1) % 4
        elif mov =='L':
            focus = (focus-1) % 4

    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
