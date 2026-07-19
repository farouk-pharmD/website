# Farouk Ashraf Portfolio

Personal portfolio and essay site for Farouk Ashraf. Built as static HTML/CSS/JS so it is easy to edit, host on GitHub Pages, and keep free of heavy tooling.

Live site: [farouk-pharmd.github.io/website](https://farouk-pharmd.github.io/website/)

## Structure

```
index.html              # Portfolio homepage
blog.html               # Essay index (“Mein Lounge”)
blogs/
  template.html         # Copy this for new posts (noindex)
  the-alignment-problem.html
Assets/
  css/style.css         # Design tokens, layout, themes, animations
  js/
    theme-preloader.js  # Applies saved/system theme before paint
    main.js             # Nav, footer, theme, audio, cursor, reveals
  portrait.jpg
  btn-download.pdf
pharmacy.ico
.github/workflows/pages.yml
```

## Page sections (homepage)

1. Hero  
2. About  
3. Experience  
4. BMCA role  
5. Skills  
6. Technical side  
7. Hobbies  
8. Contact  

When adding or removing a section, update both the navigation links in `Assets/js/main.js` and the visible section numbers in the HTML.

## Styling

CSS is organized by system: design tokens, cursor, navigation, page sections, dark theme, animations, responsive breakpoints, and blog layout.

Reuse utility classes before adding inline styles:

- `text-rust`, `text-paper`
- `skill-feature`, `skill-note`, `skill-narrative`
- Blog: `blog-post-hero`, `blog-post-title`, `blog-post-meta`, `blog-content-container`

## JavaScript

`main.js` handles:

- Shared nav + footer injection (works from nested blog paths via `data-root-path`)
- Theme preference and light/dark toggle
- Mobile navigation
- Custom cursor (fine-pointer devices only; respects reduced motion)
- Scroll reveal (once per element)
- Lazy YouTube background audio (loads only after the user presses play)
- Page transition loader
- Terminal easter egg (press `` ` ``)

The native cursor is only hidden after the custom cursor initializes, so a JS failure does not leave the pointer missing.

## Writing a blog post

1. Copy `blogs/template.html` to a new file (e.g. `blogs/my-essay.html`).
2. Update the title, meta description, canonical URL, and body.
3. Remove `noindex` if present (template includes it).
4. Add a card on `blog.html` pointing at the new file.

## Asset rule

Do not paste base64 images, PDFs, or other media into HTML. Put media in `Assets/` and link to it.

## Deploy

Pushes to `main` deploy via GitHub Pages (`.github/workflows/pages.yml`).
