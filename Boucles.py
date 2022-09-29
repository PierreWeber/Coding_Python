## garder un boucle ouverte

while True:
    line = input('> ')
    if line == 'stop' :
        break               # sort de la boucle
    print(line)
print('Over ! Done ! ')

# garder un boucle puis sortir

while True:
    line = input('> ')
    if line[0] == '#' :
        continue            # garde la boucle
    if line == 'stop' :
        break               # sort de la boucle
    print(line)
print('Over ! Done ! ')
