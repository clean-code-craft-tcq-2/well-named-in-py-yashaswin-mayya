from Colors_Initialize import color_lookup

def color_pair_to_string(major_color, minor_color):

  return f'{major_color}\t\t{minor_color}'

def ref_manual():
    
    print('################# Reference Manual #################')
    print('Major Color\tMinor Color\tPair Number')
    pair_id = 1
    for major_color in color_lookup().MAJOR_COLORS:
        for minor_color in color_lookup().MINOR_COLORS:
            print(f'{color_pair_to_string(major_color, minor_color)}\t\t{pair_id}')
            pair_id += 1