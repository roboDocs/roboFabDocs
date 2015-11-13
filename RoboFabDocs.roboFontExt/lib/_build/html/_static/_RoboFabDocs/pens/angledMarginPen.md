angledMarginPen
===============

## AngledMarginPen(glyphSet, width, italicAngle)

Pen to calculate the margins according to a slanted coordinate system. Slant angle comes from `font.info.italicAngle`.

- this pen works on the on-curve points, and approximates the distance to curves.
- results will be float.
- when used in FontLab, the resulting margins may be slightly different from the values originally set, due to rounding errors.

Notes:

- similar to what RoboFog used to do.
- RoboFog had a special attribute for “italicoffset”, horizontal shift of all glyphs. This is missing in Robofab.

### AngledMarginPen.addComponent(glyphName, transformation)

This default implementation simply transforms the points of the base glyph and draws it onto self.

## getAngledMargins(glyph, font)

Convenience function, returns the angled margins for this glyph.

Adjusted for `font.info.italicAngle`.

## setAngledLeftMargin(glyph, font, value)

Convenience function, sets the left angled margin to value.

Adjusted for `font.info.italicAngle`.

## setAngledRightMargin(glyph, font, value)

Convenience function, sets the right angled margin to value.

Adjusted for `font.info.italicAngle`.

## centerAngledMargins(glyph, font)

Convenience function, centers the glyph on angled margins.
