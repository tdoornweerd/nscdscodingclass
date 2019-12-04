from sympy import Eq, Symbol, solve
to_find = input('type the side you want to fine(L1,L2 or H): ')
if to_find == 'H':
    leg_one = input('leg one ')
    leg_one = int(leg_one,10)
    leg_two = input('leg two ')
    leg_two = int(leg_two,10)
    y = Symbol('y')
    eqn = Eq(leg_two**2 + leg_one**2, y**2)
    solve = solve(eqn)
    print('your side is equal to: ',solve[1])
    exit()
if to_find  == 'L1':
    hyp = input('hype ')
    hyp = int(hyp,10)

    leg_two = input('leg two ')
    leg_two = int(leg_two,10)
    y = Symbol('y')
    eqn = Eq(leg_two**2 + y**2, hyp**2)
    solve = solve(eqn)
    print('your side is equal to: ',solve[1])
    exit()
if to_find == 'L2':
    hyp = input('hype ')
    hyp = int(hyp,10)

    leg_one = input('leg one ')
    leg_one = int(leg_one,10)
    y = Symbol('y')
    eqn = Eq(leg_one**2 + y**2, hyp**2)
    solve = solve(eqn)
    print('your side is equal to: ',solve[1])
    exit()