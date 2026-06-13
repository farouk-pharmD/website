# Farouk Ashraf Portfolio

Single-page personal portfolio for Farouk Ashraf. The site is intentionally built as one `index.html` file with external media in `Assets/` so it is easy to edit, easy to host statically, and small enough to work on without dragging embedded base64 media through every change.

## Structure

- `index.html` contains the page markup, CSS, and JavaScript.
- `Assets/hero-portrait.jpg` is the hero portrait used by the page.
- `Assets/btn-download.pdf` is linked by the Download CV button.
- `pharmacy.ico` is the browser favicon.

## Page Sections

The page is ordered as a narrative:

1. Hero
2. About
3. Experience
4. BMCA role
5. Skills
6. Technical side
7. Hobbies
8. Contact

When adding or removing a section, update both the navigation links and the visible section numbers.

## Styling Notes

The CSS is organized by page system: design tokens, cursor, navigation, page sections, dark theme, animations, and responsive breakpoints. Reuse existing utility classes such as `skill-feature`, `skill-note`, and `text-rust` before adding inline styles.

## JavaScript Notes

The JavaScript handles four behaviors:

- Theme preference and the light/dark toggle.
- Mobile navigation open/close behavior.
- Custom cursor animation for fine-pointer devices only.
- Scroll reveal animations for sections and hero content.

The native cursor is only hidden after the custom cursor initializes, which prevents the cursor from disappearing if JavaScript fails.

## Asset Rule

Do not paste base64 images, PDFs, or other media into `index.html`. Put media files in `Assets/` and link to them from the HTML.
