# Slideshow gallery — prototype notes

**Question being answered:** What should a drop-in folder gallery *look like* for easy
viewing? Grid? One-at-a-time slideshow? Something else?

**Shape:** UI prototype (impeccable-prototype → UI.md, sub-shape B — no host app exists yet).
Three structurally different layouts live in one `index.html`, switchable via `?variant=`
or the floating bottom bar / `[` `]` keys.

| Variant | Layout | Primary affordance |
|--------|--------|--------------------|
| **A** | Masonry grid (Pinterest-style columns) | scan many at once → click for lightbox |
| **B** | Fullscreen slideshow + filmstrip + autoplay | one image at a time, ← → to move |
| **C** | Justified rows (Flickr-style, full-bleed) | dense browsing, no cropping → lightbox |

## How to run
```
cd into this folder
python3 -m http.server 8000
open http://localhost:8000
```
Images in the folder auto-load (server directory listing is parsed). If opened directly
(`file://`), use the "Pick folder" button or drag-drop — browsers can't list sibling
files from a static page.

## Sample images
`sample-01.png` … `sample-08.png` are throwaway gradient placeholders so you can
evaluate the layouts immediately. Delete them and drop your own images in:
`rm sample-*.png`

## Throwaway / fold-in plan
This is prototype code: no build step, no tests, minimal error handling. Once a layout
wins, rewrite *that one* cleanly and delete the other two + the switcher + the fallback
chrome.

## VERDICT — _fill in after flipping through_
- Winning variant:
- Why:
- Bits to steal from the others:
