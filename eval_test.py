# for a string literal to make it through eval(),
# you have to code it like this: '"string value"'

d = {'abc': ('def', 'print("xyz")'),
     'def': ('uvw', '"xxx"')
     }

print(d['abc'][1])
eval(d['abc'][1])

print(d['def'][1])
print(eval(d['def'][1]))
