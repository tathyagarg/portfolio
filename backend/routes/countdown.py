from fastapi import APIRouter
from fastapi.responses import Response
from PIL import Image, ImageDraw, ImageFont

import io
import time

IMAGE_SIZE: tuple[int, int] = (512, 512)
FONT_SIZE: int = 200
BG_COLOR: tuple[int, int, int] = (25, 25, 25)

router = APIRouter(prefix='/countdown')

@router.get('/to', responses={
    200: {
        'content': {'image/png': {}}
    },
}, response_class=Response)
def countdown_to(to: int):
    now = int(time.time())
    delta = to - now
    text = str(delta // 86_400)

    img = Image.new(mode='RGB', size=IMAGE_SIZE, color=BG_COLOR)
    font = ImageFont.truetype('font.ttf', FONT_SIZE)

    # FONT SIZE CALCULATIONS

    canvas = Image.new(mode='RGB', size=IMAGE_SIZE)
    draw = ImageDraw.Draw(canvas)
    draw.text(
        xy=(0, 0),
        text=text,
        font=font
    )

    bbox = canvas.getbbox()

    # END FONT SIZE CALCULATIONS

    x_offset: int = (512 - bbox[2] - bbox[0]) // 2
    y_offset: int = (512 - bbox[3] - bbox[1]) // 2

    drawable = ImageDraw.Draw(img)
    drawable.text(
        xy=(x_offset, y_offset),
        text=text,
        fill=(255, 255, 255),
        font=font
    )

    byte_array = io.BytesIO()
    img.save(byte_array, format='png')
    byte_array = byte_array.getvalue()

    return Response(content=byte_array, media_type='image/png')


