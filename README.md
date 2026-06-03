# slide-show

A drop-in image gallery. Put it in a folder full of pictures, run one command, and
browse them in your browser — masonry grid, fullscreen slideshow, or justified rows.

No build step, no dependencies, no config. Just Python 3 (already on macOS and most
Linux) and a folder of images.

## Quick start

```sh
cd /folder/with/your/images
python3 serve.py
```

This serves the folder and opens `http://localhost:8000`, auto-loading every image
it finds. Pass a port to use a different one: `python3 serve.py 9000`.

Drop `index.html` and `serve.py` into any image folder and the same command works there.

## Layouts

Switch with the floating bar at the bottom, the `[` and `]` keys, or a `?variant=`
URL parameter:

- **A — Masonry grid** (`?variant=A`) — Pinterest-style columns. Scan a lot at once;
  click any image for a lightbox. Arrow keys move through the lightbox.
- **B — Fullscreen slideshow** (`?variant=B`) — one image at a time with a thumbnail
  filmstrip. `←` / `→` to move, `▶ Play` for autoplay.
- **C — Justified rows** (`?variant=C`) — Flickr-style rows that fill the width at a
  uniform height, no cropping. Click for the lightbox.

Images are sorted naturally (`img2` before `img10`). Supported: jpg, jpeg, png, gif,
webp, avif, bmp, svg.

## How it finds images

`serve.py` static-serves the folder and adds one route, `/__images`, that returns the
image filenames as JSON. The page fetches that on load. (A plain static server can't do
this — it returns `index.html` at `/` instead of a file list, so the page would never
see the images.)

If you open `index.html` directly over `file://` instead of running the server, it falls
back to a drag-and-drop zone and a "Pick a folder" button, since browsers can't list a
folder's contents from a static page.

## Files

| File         | Purpose                                          |
|--------------|--------------------------------------------------|
| `index.html` | The gallery — all three layouts in one page      |
| `serve.py`   | Local server that serves the folder and finds images |
