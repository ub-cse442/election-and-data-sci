import simplemapplot


def simplemap():

    colors = ["#FF0000", "#0000FF", "#800080"]  # 0 = Red, 1 = Blue, 2 = Purple

    states = {}
    blue_states = {}
    red_states = {}
    purple_states = {}

    states["AL"] = 0
    states["AK"] = 0
    states["AZ"] = 0
    states["AR"] = 0
    states["CA"] = 1
    states["CO"] = 1
    states["CT"] = 1
    states["DE"] = 1
    states["FL"] = 2
    states["GA"] = 0
    states["HI"] = 1
    states["ID"] = 0
    states["IL"] = 1
    states["IN"] = 0
    states["IA"] = 0
    states["KS"] = 0
    states["KY"] = 0
    states["LA"] = 0
    states["ME"] = 1
    states["MD"] = 1
    states["MA"] = 1
    states["MI"] = 1
    states["MN"] = 1
    states["MS"] = 0
    states["MO"] = 0
    states["MT"] = 0
    states["NE"] = 0
    states["NV"] = 2
    states["NH"] = 1
    states["NJ"] = 1
    states["NM"] = 1
    states["NY"] = 1
    states["NC"] = 2
    states["ND"] = 0
    states["OH"] = 2
    states["OK"] = 0
    states["OR"] = 1
    states["PA"] = 1
    states["RI"] = 1
    states["SC"] = 0
    states["SD"] = 0
    states["TN"] = 0
    states["TX"] = 0
    states["UT"] = 0
    states["VT"] = 1
    states["VA"] = 1
    states["WA"] = 1
    states["WV"] = 0
    states["WI"] = 1
    states["WY"] = 0


    simplemapplot.make_us_state_map(data=states, colors=colors)

simplemap()
