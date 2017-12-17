import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import pymunk.pygame_util
import pymunk.autogeometry
import numpy as np
import random
import csv


def add_static_L(space):

    floor0 = pymunk.Segment(space.static_body, (-10, 5000), (0, 150), 5)
    floor0.friction = 1.0

    floor = pymunk.Segment(space.static_body, (0, 150), (300, 200), 5)
    floor.friction = 1.0

    floor1 = pymunk.Segment(space.static_body, (300, 200), (350, 250), 5)
    floor1.friction = 1.0

    floor2 = pymunk.Segment(space.static_body, (350, 250), (380, 260), 5)
    floor2.friction = 1.0

    floor3 = pymunk.Segment(space.static_body, (380, 260), (480,200), 5)
    floor3.friction = 1.0

    floor4 = pymunk.Segment(space.static_body, (480, 200), (540, 200), 5)
    floor4.friction = 1.0

    floor5 = pymunk.Segment(space.static_body, (540, 200), (600, 250), 5)
    floor5.friction = 1.0

    floor6 = pymunk.Segment(space.static_body, (600,250), (700, 250), 5)
    floor6.friction = 1.0

    floor7 = pymunk.Segment(space.static_body, (700, 250), (740, 280), 5)
    floor7.friction = 1.0

    floor8 = pymunk.Segment(space.static_body, (740, 280), (820, 380), 5)
    floor8.friction = 1.0

    floor9 = pymunk.Segment(space.static_body, (820, 380), (860, 380), 5)
    floor9.friction = 1.0

    floor10 = pymunk.Segment(space.static_body, (860, 380), (880, 180), 5)
    floor10.friction = 1.0

    floor11 = pymunk.Segment(space.static_body, (880, 180), (1000, 180), 5)
    floor11.friction = 1.0

    floor12 = pymunk.Segment(space.static_body, (1000, 180), (1100, 250), 5)
    floor12.friction = 1.0

    floor13 = pymunk.Segment(space.static_body, (1100, 250), (1140, 210), 5)
    floor13.friction = 1.0

    floor14 = pymunk.Segment(space.static_body, (1140, 210), (1180, 250), 5)
    floor14.friction = 1.0

    floor15 = pymunk.Segment(space.static_body, (1180, 250), (1220, 210), 5)
    floor15.friction = 1.0

    floor16 = pymunk.Segment(space.static_body, (1220, 210), (1260, 250), 5)
    floor16.friction = 1.0

    floor17 = pymunk.Segment(space.static_body, (1260, 250), (1300, 210), 5)
    floor17.friction = 1.0

    floor18 = pymunk.Segment(space.static_body, (1300, 210), (1400, 210), 5)
    floor18.friction = 1.0

    floor19 = pymunk.Segment(space.static_body, (1400, 210), (1550, 400), 5)
    floor19.friction = 1.0

    floor20 = pymunk.Segment(space.static_body, (1550, 400), (1650, 400), 5)
    floor20.friction = 1.0

    floor21 = pymunk.Segment(space.static_body, (1650, 400), (1700, 10000), 5)
    floor21.friction = 1.0



    space.add(floor0, floor, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8,floor9,floor10,floor11,floor12,floor13,floor14,floor15,floor16,floor17,floor18,floor19, floor20, floor21)

    return floor0, floor, floor1, floor2, floor3, floor4, floor5, floor6, floor7, floor8,floor9,floor10,floor11,floor12,floor13,floor14,floor15,floor16,floor17,floor18,floor19, floor20, floor21


def car(space, wheel_mass, wheel_radius, density, wheel1_pos, wheel2_pos, wheel_friction, speed1, speed2, pinjoint1_1, pinjoint1_2, pinjoint2_1, pinjoint2_2):
    pos = Vec2d(100, 200)

    # wheel_mass = 100  #arguments
    # wheel_radius = 12
    chassi_size_x = 50
    chassi_size_y = 16
    # density = 20
    # wheel1_pos = 35      #24.5
    # wheel2_pos = 35
    # wheel_friction = 1.5
    # speed1 = 15
    # speed2 = 15
    # pinjoint1_1 = 20, 10  #joints position
    # pinjoint1_2 = -20, 10
    # pinjoint2_1 = -20, 10
    # pinjoint2_2 = 20, 10

    field = chassi_size_y * chassi_size_x
    size = (chassi_size_x,chassi_size_y)
    chassi_mass = field * density
    wheel_color_1 = 255, 0, 100
    wheel_color_2 = 0, 0, 0

    moment = pymunk.moment_for_circle(wheel_mass, 20, wheel_radius)
    wheel1_b = pymunk.Body(wheel_mass, moment)
    wheel1_s = pymunk.Circle(wheel1_b, wheel_radius)
    wheel1_s.friction = wheel_friction
    wheel1_s.color = wheel_color_1

    space.add(wheel1_b, wheel1_s)

    moment = pymunk.moment_for_circle(wheel_mass, 20, wheel_radius)
    wheel2_b = pymunk.Body(wheel_mass, moment)
    wheel2_s = pymunk.Circle(wheel2_b, wheel_radius)
    wheel2_s.friction = wheel_friction
    wheel2_s.color = wheel_color_2
    space.add(wheel2_b, wheel2_s)


    moment = pymunk.moment_for_box(chassi_mass, size)

    chassi_b = pymunk.Body(wheel_mass, moment)
    chassi_s = pymunk.Poly.create_box(chassi_b, size)
    chassi_s.friction = 2.5
    space.add(chassi_b, chassi_s)


    wheel1_b.position = pos + (-wheel1_pos , 0)
    wheel2_b.position = pos + (wheel2_pos , 0)
    chassi_b.position = pos + (0, 25)


    rest_length_1 = 1
    rest_length_2 = 1
    stiffness_1 = 40
    stiffness_2 = 40
    damping_1 = 200
    damping_2 = 200

    # angle = 0
    # gr = pymunk.GrooveJoint(chassi_b, wheel1_b, (-25,-8), (-24,-8), (0,0))
    # gf = pymunk.GrooveJoint(chassi_b, wheel2_b, (25,-8), (24,-8), (0,0))
    #
    # dru = pymunk.DampedSpring(wheel1_b, chassi_b, (0, 0), (-25, 8), rest_length_1, stiffness_1 , damping_1)    #rest_length, stiffness(young moduke), damping
    # dfu = pymunk.DampedSpring(wheel2_b, chassi_b, (0, 0), (25, 8), rest_length_1, stiffness_1 , damping_1)
    #
    # drc = pymunk.DampedSpring(wheel1_b, chassi_b, (0, 0), (20, -10), rest_length_2, stiffness_2 , damping_2)
    # dfc = pymunk.DampedSpring(wheel2_b, chassi_b, (0, 0), (-20, -10), rest_length_2, stiffness_2 , damping_2)

    space.add(
        #pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), (-15, -15)),
        #pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), (15, -15)),
        pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), pinjoint1_1),
        pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), pinjoint1_2),

        pymunk.PinJoint(wheel1_b, chassi_b, (0, 0), pinjoint2_1),
        pymunk.PinJoint(wheel2_b, chassi_b, (0, 0), pinjoint2_2)

    )

    space.add(
       pymunk.SimpleMotor(wheel1_b, chassi_b, -speed1),
       pymunk.SimpleMotor(wheel2_b, chassi_b, -speed2)
    )

    return wheel1_b

def los_probki(il_arg, il_probek, mins, maxs):

    M = np.zeros((il_probek, il_arg))

    for p in range(0, il_probek):

        for ar in range(0, il_arg):

            M[p, ar] = random.uniform(mins[ar], maxs[ar])

    return M


def simulate(wheel_mass, wheel_radius, density, wheel1_pos, wheel2_pos, wheel_friction, speed1, speed2, pinjoint1_1, pinjoint1_2, pinjoint2_1, pinjoint2_2):
    pygame.init()
    screen = pygame.display.set_mode((1800, 1000))
    pygame.display.set_caption("They see me rollin")
    clock = pygame.time.Clock()
    '''
    space = pymunk.Space()
    space2 = pymunk.Space()

    space.gravity = (0.0, -900.0)
    space2.gravity = (0.0, -900.0)

    lines = add_static_L(space)
    lines = add_static_L(space2)

    track = car(space, wheel_mass, wheel_radius, chassi_size_x, chassi_size_y, density,
        wheel1_pos, wheel2_pos, wheel_friction, speed1, speed2, pinjoint1_1, pinjoint1_2, pinjoint2_1, pinjoint2_2)

    track2 = car(space2, wheel_mass, wheel_radius, chassi_size_x, chassi_size_y, density,
        wheel1_pos, wheel2_pos, wheel_friction, speed1, speed2, pinjoint1_1, pinjoint1_2, pinjoint2_1, pinjoint2_2)'''
    amount = 1000
    final = [0] * amount
    space = [0] * amount
    track = [0] * amount
    probka = los_probki(17, amount, [10,6,10,15,15,1,0,0,   -25,-8,-25,-8,-25,-8,-25,-8,    0], [100,17,60,45,45,3,15,15,   25,8,25,8,25,8,25,8,   0])
    for i in range(amount):
         space[i] = pymunk.Space()
         space[i].gravity = (0.0, -900.0)
         lines = add_static_L(space[i])
         track[i] = car(space[i], probka[i][0], probka[i][1], probka[i][2], probka[i][3], probka[i][4], probka[i][5], probka[i][6], probka[i][7],
                                  (probka[i][8], probka[i][9]), (probka[i][10], probka[i][11]), (probka[i][12], probka[i][13]), (probka[i][14], probka[i][15]))


    draw_options = pymunk.pygame_util.DrawOptions(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        screen.fill((255,255,255))

        space[0].debug_draw(draw_options)
        for i in range(amount):
            space[i].step(1/50.0)

        pygame.display.flip()
        clock.tick(50)
        time = pygame.time.get_ticks()/1000
        if time > 12:
            for i in range(amount):
                if int(track[i].position[0]) > 0 and int(track[i].position[0]) < 1700:
                    probka[i][16] =  int(track[i].position[0])

            break
    for i in range(amount):
        print probka[i][16]

    csv_file=open("nowa_paczka.csv",'a')
    wr = csv.writer(csv_file)
    wr.writerows(probka)







if __name__ == '__main__':
    print simulate(100, 17, 40, 40, 40, 1.5, 15, 15, (20,10), (-20,10), (-20,10), (20,10))
