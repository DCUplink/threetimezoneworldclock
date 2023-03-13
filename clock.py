import sys
import os
from datetime import datetime, timedelta
import pytz
from PIL import Image, ImageFont, ImageDraw
import tkinter as tk
from PIL import ImageTk
from font_fredoka_one import FredokaOne

clocks = [  'America/New_York',  'Europe/London',  'Asia/Calcutta',]

window = tk.Tk()
window.title("Clocks")
canvas = tk.Canvas(window, width=2000, height=720)
canvas.pack()

img = Image.new('RGB', (2000, 720), color='black')
draw = ImageDraw.Draw(img)

big_font = ImageFont.truetype(FredokaOne, 120)
small_font = ImageFont.truetype(FredokaOne, 120)

x = 341
y = 240

def update_clock():
  global img, draw, big_font, small_font, x, y, clocks, canvas
  img = Image.new('RGB', (2000, 720), color='black')
  draw = ImageDraw.Draw(img)
  idx = 1
  for clock in clocks:
    tz = os.environ.get('TZ', clock)
    tz_obj = pytz.timezone(tz)
    now = datetime.now(tz=tz_obj)
    city = clock.split('/')[1].replace('_', ' ')
    ctime = now.strftime('%a,%H:%M:%S')

    draw.text((15, (idx*y)-y+10), city, fill=(13, 54, 5), font=small_font)
    draw.text((650, (idx*y)-y+7), str(ctime.split(',')[0]), fill=(13, 54, 5), font=big_font)
    draw.text((1100, (idx*y)-y+7), str(ctime.split(',')[1]), fill=(13, 54, 5), font=big_font)
    draw.text((1400, (idx*y)-y+7), str(ctime.split(',')[2]) if len(ctime.split(',')) > 2 else '', fill=(13, 54, 5), font=big_font)

    idx += 1

  img_tk = ImageTk.PhotoImage(image=img)
  canvas.create_image(0, 0, anchor="nw", image=img_tk)
  canvas.img_tk = img_tk
  window.after(1000, update_clock)
  

update_clock()

window.mainloop()
