import click
from PIL import Image

from . import core


@click.command()
@click.argument('image_path', metavar='IMAGE_PATH', type=str)
@click.argument('text', metavar='WATERMARK_TEXT', type=str)
@click.argument('output', metavar='OUTPUT_PATH', type=str)
@click.option('--font', '-f', type=str, show_default=True, default=None)
@click.option('--font-size', '-s', type=int, show_default=True, default=28)
@click.option('--font-index', type=int, show_default=True, default=0)
@click.option('--spacing', '-S', type=int, show_default=True, default=4)
@click.option('--align', '-A', type=str, show_default=True, default='center')
@click.option('--color', '-c', type=str, show_default=True, default='#000000')
@click.option('--alpha', '-a', type=float, show_default=True, default=0.2)
@click.option('--rotate', '-r', type=float, show_default=True, default=-30)
@click.option('--width', '-w', 'stamp_width', type=int, show_default=True, default=350)
@click.option('--height', '-h', 'stamp_height', type=int, show_default=True, default=200)
@click.option('--quality', '-q', type=int, show_default=True, default=90)
def watermark(**kwargs):
    image_path = kwargs.pop('image_path')
    output = kwargs.pop('output')
    quality = kwargs.pop('quality')

    image = Image.open(image_path)
    core.watermark(image=image, **kwargs).save(output, quality=quality)


if __name__ == '__main__':
    watermark()
