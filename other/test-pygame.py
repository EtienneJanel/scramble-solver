import sys, pygame

pygame.init()

TILESIZE = 100
BOARD_POS = (100, 100)

black = 0,0,0
screen = pygame.display.set_mode((700,700))

def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*3, TILESIZE*3))
    dark = False
    for y in range(4):
        for x in range(4):
            rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('darkgrey' if dark else 'beige'), rect)
            dark = not dark
        dark = not dark
    return board_surf

def create_board():
    board = []
    for y in range(4):
        board.append([])
        for x in range(4):
            board[y].append(None)
            
    for x in range(0, 3):
        board[0][x] = ('black', 'pawn')
    for x in range(0, 3):
        board[3][x] = ('white', 'pawn') 
    return board

def draw_pieces(screen, board, selected_piece):
    sx, sy = None, None
    if selected_piece:
        piece, sx, sy = selected_piece

    for y in range(3):
        for x in range(3): 
            piece = board[y][x]
            if piece:
                selected = x == sx and y == sy
#                 color, type = piece
#                 s1 = font.render(type[0], True, pygame.Color('red' if selected else color))
#                 s2 = font.render(type[0], True, pygame.Color('darkgrey'))
#                 pos = pygame.Rect(BOARD_POS[0] + x * TILESIZE+1, BOARD_POS[1] + y * TILESIZE + 1, TILESIZE, TILESIZE)
                screen.blit(s2, s2.get_rect(center=pos.center).move(1, 1))
                screen.blit(s1, s1.get_rect(center=pos.center))

tux = pygame.image.load('orangutan_1f9a7.png')
tux = pygame.transform.scale(tux, (100,100))

x = 0
y = 0


selected_piece = None
board = create_board()
board_surf = create_board_surf()
drop_pos = None

while True:
#     screen.blit(tux, (x+50,y+50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected_piece != None:
                x,y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if drop_pos:
                piece, old_x, old_y = selected_piece
                board[old_y][old_x] = 0
                new_x, new_y = drop_pos
                board[new_y][new_x] = piece
            selected_piece = None
            drop_pos = None

    screen.fill(black)
    screen.blit(board_surf, (0,0))
#     screen.blit(tux, (x+50,y+50))
    draw_pieces(screen, board, selected_piece)
    
    pygame.display.flip()

    