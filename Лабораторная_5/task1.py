# TODO решить с помощью list comprehension и распечатать его
import pprint;

l = list()
for i in range(16):
    l.append({'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)})
pprint.pprint(l)