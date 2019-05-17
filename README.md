# watermarking

Watermark your image.

**Sketch. Not ready for distribution or production use.**

## Installation

```bash
$ git clone https://github.com/microdog/watermarking.git
$ cd watermarking
$ python setup.py install
```

## Usage

```bash
$ watermarking --help
Usage: watermarking [OPTIONS] IMAGE_PATH WATERMARK_TEXT OUTPUT_PATH

Options:
  -f, --font TEXT
  -s, --font-size INTEGER  [default: 28]
  --font-index INTEGER     [default: 0]
  -S, --spacing INTEGER    [default: 4]
  -A, --align TEXT         [default: center]
  -c, --color TEXT         [default: #000000]
  -a, --alpha FLOAT        [default: 0.2]
  -r, --rotate FLOAT       [default: -30]
  -w, --width INTEGER      [default: 350]
  -h, --height INTEGER     [default: 200]
  -q, --quality INTEGER    [default: 90]
  --help                   Show this message and exit.
```

## TODO

- [ ] Query font by name or ship a bundled font
