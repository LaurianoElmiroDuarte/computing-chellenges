def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    return dsquared

print('{}'.format(distance(3,4,4,5)))
