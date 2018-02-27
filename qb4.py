print('Calculator')
print('Options:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5.Exit')
opt = (input('Enter operator:'))
a = float(input('Enter operands:\n')) 
b = float(input())
def calc(a, b, opt):
    return {
        '+' : a+b,
        '-' : a-b,
        '*' : a*b,
        '/' : a/b,	
    }.get(opt, 'Invalid Operator')
print(calc(a,b,opt))

