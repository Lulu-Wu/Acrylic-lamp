from globalVal import globalVal,const

def coordinate_map(x, y):
    if x >= const.MIN_HEIGHT_BG and x < const.MAX_HEIGHT_BG and y >= const.MIN_WIDTH_BG and y < const.MAX_WIDTH_BG:
        if (y % 2) == 0:
            point = x + 4 * (3 - y)
        else:
            point = (3 - x) + 4 * (3 - y)
    else:
        point = -1
    return point