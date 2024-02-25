import argparse
from cowsay import cowsay, list_cows, Option


prs = argparse.ArgumentParser()

prs.add_argument("-e", dest='eye_string', default=Option.eyes)
prs.add_argument("-f", dest='cowfile', type=str, default='default')
prs.add_argument("-l", action='store_true')
prs.add_argument("-n", action='store_false')
prs.add_argument("-T", dest='tongue_string', default=Option.tongue)
prs.add_argument("-W", dest='column', type=int, default=40)
prs.add_argument("message", nargs='*', default=[' '])

prs.add_argument('-b', action='store_true', help='С коровой (-b)')
prs.add_argument('-d', action='store_true', help='С забором (-d)')
prs.add_argument('-g', action='store_true', help='С глазами (-g)')
prs.add_argument('-p', action='store_true', help='С языком (-p)')
prs.add_argument('-s', action='store_true', help='С языком в сторону (-s)')
prs.add_argument('-t', action='store_true', help='С трубой (-t)')
prs.add_argument('-w', action='store_true', help='С волнами (-w)')
prs.add_argument('-y', action='store_true', help='С лапкой (-y)')


args = prs.parse_args()

ops = ''
for op in 'bdgpstwy':
    if getattr(args, op):
        ops += f'{op}'

if args.l is False:
    if '/' in args.cowfile:
        s, f = '', open(args.cowfile, "r")
		
		while val:=f.readline():
			s += val

        print(cowsay(' '.join(args.message), preset=options, eyes=args.eye_string, tongue=args.tongue_string, width=args.column, wrap_text=args.n, cowfile=s))

    else:
        print(cowsay(' '.join(args.message), cow=args.cowfile, preset=options, eyes=args.eye_string, tongue=args.tongue_string, width=args.column, wrap_text=args.n))
  
else:
    print(*list_cows())