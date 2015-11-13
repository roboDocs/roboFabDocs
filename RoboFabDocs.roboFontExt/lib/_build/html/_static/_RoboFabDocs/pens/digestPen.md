digestPen
=========

## class DigestPointPen(ignoreSmoothAndName=False)

This calculates a tuple representing the structure and values in a glyph:

- including coordinates  
- including components  

Example:

	from robofab.pens.digestPen import DigestPointPen  
	pen = DigestPointPen()  
	g = CurrentGlyph()  
	g.drawPoints(pen)  
	pen.getDigest()  

	>>> ('beginPath', ((25, 425), 'line', False, None),((25, 0), 'line', False, None),((95, 0), 'line', False, None),((95, 425), 'line', False, None), 'endPath', 'beginPath', ((25, 595), 'line', False, None),((25, 491), 'line', False, None),((95, 491), 'line', False, None),((95, 595), 'line', False, None), 'endPath')  

### getDigest()

Return the digest as a tuple with all coordinates of all points.

### getDigestPointsOnly(needSort=True)

Return the digest as a tuple with all coordinates of all points, - but without smooth info or drawing instructions. - For instance if you want to compare 2 glyphs in shape, but not interpolatability.

## class DigestPointStructurePen(ignoreSmoothAndName=False)

This calculates a tuple representing the structure and values in a glyph:

- excluding coordinates
- excluding components

Example:

	from robofab.pens.digestPen import DigestPointStructurePen  
	pen = DigestPointStructurePen()  
	g = CurrentGlyph()  
	g.drawPoints(pen)  
	pen.getDigest()  

	>>> ('beginPath', 'line', 'line', 'line', 'line', 'endPath', 'beginPath', 'line', 'line', 'line', 'line', 'endPath')  

### getDigest()

Return the digest as a tuple with all coordinates of all points.

### getDigestPointsOnly(needSort=True)

Return the digest as a tuple with all coordinates of all points, - but without smooth info or drawing instructions. - For instance if you want to compare 2 glyphs in shape, but not interpolatability.
