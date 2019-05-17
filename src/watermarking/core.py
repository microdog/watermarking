from typing import Optional, Union

from PIL import Image, ImageColor, ImageDraw, ImageFont


def _load_font(font, index, size) -> ImageFont:
    return ImageFont.truetype(font, size=size, index=index) if font else ImageFont.load_default()


def _wrap_text(image_draw: ImageDraw, text, width, max_lines=0, ellipsis='...', **kwargs):
    lines = []
    line = ''
    for token in iter(text):
        if len(lines) >= max_lines > 0:
            # TODO calculate the actual width
            lines[-1] = lines[-1][: -len(ellipsis)] + ellipsis
            break

        if token in '\r\n':
            lines.append(line)
            continue

        newline = line + token
        size = image_draw.textsize(newline, **kwargs)
        if size[0] < width:
            line = newline
            continue

        lines.append(line)
        line = token
    else:
        lines.append(line)
    return lines


def _create_stamp(font: ImageFont, text, spacing, align, color, rotate, width, height):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    text = '\n'.join(_wrap_text(draw, text, width, max_lines=-1, font=font))
    text_width, text_height = draw.multiline_textsize(text, font, spacing)

    draw.multiline_text(
        ((width - text_width) / 2.0, (height - text_height) / 2.0),
        text,
        fill=color,
        font=font,
        spacing=spacing,
        align=align,
    )

    return image.rotate(rotate, resample=Image.BICUBIC, expand=False, fillcolor=(0, 0, 0, 0))


def _create_stamp_layer(
    image: Image.Image, font: ImageFont, text, spacing, align, color, rotate, width, height
):
    stamp = _create_stamp(font, text, spacing, align, color, rotate, width, height)
    layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for y in range(-height // 2, layer.height, height):
        for x in range(-width // 2, layer.width, width):
            layer.paste(stamp, (x, y))
    return layer


def watermark(
    image: Image.Image,
    text: str,
    font: Optional[Union[str, ImageFont.ImageFont]] = None,
    font_index: int = 0,
    font_size: int = 24,
    spacing: int = 4,
    align: str = 'left',
    color: str = '#000000',
    alpha: float = 0.5,
    rotate: float = -35,
    stamp_width: int = 320,
    stamp_height: int = 180,
) -> Image.Image:
    # load font
    if not isinstance(font, ImageFont.ImageFont):
        font = _load_font(font, font_index, font_size)

    # apply alpha to text color
    color = ImageColor.getrgb(color) + (int(255 * alpha),)

    # convert image to RGBA mode
    image = image.convert('RGBA')

    # create stamp layer
    stamp_layer = _create_stamp_layer(
        image, font, text, spacing, align, color, rotate, stamp_width, stamp_height
    )

    # composite layers
    image.alpha_composite(stamp_layer)

    return image.convert('RGB')
