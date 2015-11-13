marginPen
=========

## class MarginPen(glyphSet, value, isHorizontal=True)

Pen to calculate the margins at a given height or width.

* `isHorizontal=True`: slice the glyph at `y=value`.
* `isHorizontal=False`: slice the glyph at `x=value`.

Example:

	f = CurrentFont()
	g = CurrentGlyph()
	pen = MarginPen(f, 200, isHorizontal=True)
	g.draw(pen)
	print pen.getMargins()

	>>> (75.7881, 181.9713)

	pen = MarginPen(f, 200, isHorizontal=False)
	g.draw(pen)
	print pen.getMargins()
	
	>>> (26.385, 397.4469)

	print pen.getAll()
	
	>>> [75.7881, 181.9713]
	
	pen = MarginPen(f, 200, isHorizontal=False)
	g.draw(pen)
	print pen.getMargins()
	
	>>> (26.385, 397.4469)
	
	print pen.getAll()
	
	>>> [26.385, 171.6137, 268.0, 397.4469]

Possible optimisation: Initialise the pen object with a list of points we want to measure, then draw the glyph once, but do the `splitLine()` math for all measure points.

### getAll()

Return all the slices.

### getContourMargins()[source]

Return the extremes of the slice for each contour.

### getMargins()

Return the extremes of the slice for all contours combined, i.e. the whole glyph.
