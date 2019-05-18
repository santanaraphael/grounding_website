from PIL import Image, ImageDraw, ImageFont
# get an image


def draw_grid(grid_height, grid_width, spacement):
    base = Image.new('RGBA', (grid_width, grid_height), (255, 255, 255, 255))
    d = ImageDraw.Draw(base)
    horizontal_lines = int(grid_width/spacement)
    vertical_lines = int(grid_height/spacement)
    hor_pos = 0
    for line in range(horizontal_lines):
        d.line([(hor_pos, 0), (hor_pos, grid_height)], fill=(0, 0, 0, 255))
        hor_pos += spacement
    ver_pos = 0
    for line in range(vertical_lines):
        d.line([(0, ver_pos), (grid_width, ver_pos)], fill=(0, 0, 0, 255))
        ver_pos += spacement
    base.save('grid.png')
    base.show()

# base = Image.new('RGBA', (400, 400), (255,255,255, 250))
#
# # make a blank image for the text, initialized to transparent text color
# txt = Image.new('RGBA', base.size, (255,255,255,100))
#
# # get a font
# fnt = ImageFont.load_default()
# # get a drawing context
# d = ImageDraw.Draw(txt)
#
# # draw text, half opacity
# d.text((10, 10), "Hello", fill=(0,0,0,128))
# # draw text, full opacity
# d.text((10, 60), "World", fill=(0,0,0,255))
#
# d.line([(0, 0), (100, 0),(200, 310)], fill=(0,0,0,255))
#
# out = Image.alpha_composite(base, txt)
#
# out.show()

draw_grid(400, 300, 10)
