import argparse
from cowsay import cowsay, Option, list_cows


parser = argparse.ArgumentParser()

parser.add_argument("-e", dest='eye_string', default=Option.eyes)
parser.add_argument("-f", dest='cowfile', type=str, default='default')
parser.add_argument("-l", action='store_true')
parser.add_argument("-n", action='store_false')
parser.add_argument("-T", dest='tongue_string', default=Option.tongue)
parser.add_argument("-W", dest='column', type=int, default=40)
parser.add_argument("message", nargs='*', default=[' '])

parser.add_argument('-b', action='store_true', help='С коровой (-b)')
parser.add_argument('-d', action='store_true', help='С забором (-d)')
parser.add_argument('-g', action='store_true', help='С глазами (-g)')
parser.add_argument('-p', action='store_true', help='С языком (-p)')
parser.add_argument('-s', action='store_true', help='С языком в сторону (-s)')
parser.add_argument('-t', action='store_true', help='С трубой (-t)')
parser.add_argument('-w', action='store_true', help='С волнами (-w)')
parser.add_argument('-y', action='store_true', help='С лапкой (-y)')


args = parser.parse_args()

ops = ''
for op in 'bdgpstwy':
    if getattr(args, op):
        ops += f'{op}'