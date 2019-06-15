import sys
import pygame
import random
from pygame.locals import *
import classes


FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BGCOLOR = (10, 10, 60)
BLACK = (0, 0, 0)
STACKBG = (200, 200, 200, 40)
cards = [i for i in range(54)]
PLAYER0X = WINDOWWIDTH / 2 - 100
PLAYER0Y =  WINDOWHEIGHT / 4 * 3
PLAYER1X = WINDOWWIDTH / 2 - 300
PLAYER1Y = WINDOWHEIGHT / 2 - 50
PLAYER2X = WINDOWWIDTH / 2 - 100
PLAYER2Y = WINDOWHEIGHT / 8
PLAYER3X =  WINDOWWIDTH / 2 - 20 + 50
PLAYER3Y = WINDOWHEIGHT / 8
PLAYER4X = WINDOWWIDTH / 2 - 20 + 240
PLAYER4Y = WINDOWHEIGHT / 2 - 50
PLAYER5X = WINDOWWIDTH / 2 - 20 + 50
PLAYER5Y = WINDOWHEIGHT / 4 * 3


def main(no_players):
    assert no_players > 1, 'Number of players must be minimum 2'
    assert no_players < 7, 'Max number of players is 6'
    step = 0
    players = [classes.Player(1/no_players, i) for i in range(no_players)]

    while True:
        pygame.init()
        global FPSCLOCK, DISPLAYSURF
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Texas Holdem No-Limit Poker")
        DISPLAYSURF.fill(BGCOLOR)

        if step == 0:
            get_cards(cards, players)
            step += 1

        if step == 1:
            draw_table()
            draw_your_hand(players[0].hand)
            for player in players:
                draw_players_reversed_cards(player)
                draw_players_stack(player)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def draw_table():
    table_img = pygame.image.load('./graphics/table4.png')
    DISPLAYSURF.blit(table_img, (0, 0))


def draw_your_hand(p_cards):
    card1_img = pygame.image.load('./graphics/' + decode_cards(p_cards[0]) + '.png')
    card2_img = pygame.image.load('./graphics/' + decode_cards(p_cards[1]) + '.png')

    DISPLAYSURF.blit(card1_img, (PLAYER0X - 20, PLAYER0Y))
    DISPLAYSURF.blit(card2_img, (PLAYER0X + 20, PLAYER0Y))


def draw_players_reversed_cards(player):
    card_img = pygame.image.load('./graphics/reverse.png')
    if player.number != 0:
        DISPLAYSURF.blit(card_img, (give_players_x_coords(player.number) - 20, give_players_y_coords(player.number)))
        DISPLAYSURF.blit(card_img, (give_players_x_coords(player.number) + 20, give_players_y_coords(player.number)))


def draw_players_stack(player):
    font_obj = pygame.font.Font('freesansbold.ttf', 15)
    stack_surface = font_obj.render(str(player.stack)[:5], True, BLACK, STACKBG)
    stack_rect = stack_surface.get_rect()
    stack_rect.center = (give_players_x_coords(player.number) + 20, give_players_y_coords(player.number) + 70)
    DISPLAYSURF.blit(stack_surface, stack_rect)


def decode_cards(nb):
    color = (nb % 4) + 1
    value = nb // 4
    if value < 8:
        value_str = str(value + 2)
    elif value == 8:
        value_str = "T"
    elif value == 9:
        value_str = "J"
    elif value == 10:
        value_str = "Q"
    elif value == 11:
        value_str = "K"
    else:
        value_str = "A"
    return value_str + str(color)


def get_cards(c, players):
    random.shuffle(c)
    for player in players:
        player.get_cards([c[0], c[1]])
        del c[:2]


def give_players_x_coords(player_nb):
    if player_nb == 0:
        return PLAYER0X
    elif player_nb == 1:
        return PLAYER1X
    elif player_nb == 2:
        return PLAYER2X
    elif player_nb == 3:
        return PLAYER3X
    elif player_nb == 4:
        return PLAYER4X
    elif player_nb == 5:
        return PLAYER5X


def give_players_y_coords(player_nb):
    if player_nb == 0:
        return PLAYER0Y
    elif player_nb == 1:
        return PLAYER1Y
    elif player_nb == 2:
        return PLAYER2Y
    elif player_nb == 3:
        return PLAYER3Y
    elif player_nb == 4:
        return PLAYER4Y
    elif player_nb == 5:
        return PLAYER5Y

def give_players_coords(player_nb):
    return give_players_x_coords(player_nb), give_players_y_coords(player_nb)

main(6)
