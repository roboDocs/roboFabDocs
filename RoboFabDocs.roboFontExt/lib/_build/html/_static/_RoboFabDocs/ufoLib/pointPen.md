pointPen
========

Where `SegmentPens` have an intuitive approach to drawing (if you’re familiar with postscript anyway), the `PointPen` is geared towards accessing all the data in the contours of the glyph. A `PointPen` has a very simple interface, it just steps through all the points in a call from `glyph.drawPoints()`. This allows the caller to provide more data for each point. For instance, whether or not a point is smooth, and its name.

## class AbstractPointPen()

Baseclass for all `PointPens`.

Should move to ufoLib?

### addComponent(baseGlyphName, transformation)

Add a sub glyph.

### addPoint(pt, segmentType=None, smooth=False, name=None, **kwargs)

Add a point to the current sub path.

### beginPath()

Start a new sub path.

### endPath()

End the current sub path.

## class BasePointToSegmentPen()

Base class for retrieving the outline in a segment-oriented way. The `PointPen` protocol is simple yet also a little tricky, so when you need an outline presented as segments but you have as points, do use this base implementation as it properly takes care of all the edge cases.

### addComponent(baseGlyphName, transformation)

Add a sub glyph.

### addPoint(pt, segmentType=None, smooth=False, name=None, **kwargs)

Add a point to the current sub path.

### beginPath()

Start a new sub path.

### endPath()

End the current sub path.
