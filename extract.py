import colorgram

colors = colorgram.extract("image.jpeg", 40)
print(colors)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    fin_color = (r, g, b)

    color_list.append(fin_color)
print(color_list)