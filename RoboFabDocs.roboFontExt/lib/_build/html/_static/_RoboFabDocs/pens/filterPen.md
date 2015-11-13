filterPen
=========

Filters: chaining pen objects

By chaining two (or more) pen objects together, the first pen can function as a filter to the second. The first pen receives data from (for instance) `glyph.draw()` or `glyph.drawPoints()`. The filter pen then processes the data and passes new, fresh data to the second pen. In turn the second pen can draw in a glyph.

Filterpens need to be initialised with a second pen object that will receive the processed data. The examples in this module, `ThresholdPen` and `FlattenPen`, have proven useful in a number of projects. For convenience, each pen has a wrapper function that takes care of making a new glyph to dump the processed data in, and making the appropriate pen instances. But these are non-normative examples.

All pens in this module subclass from `fontTools.pens.basePen`.

## class FlattenPen(otherPen, approximateSegmentLength=5, segmentLines=False, filterDoubles=True)

This filter pen processes the contours into a series of straight lines by flattening the curves.

- *otherPen*: a different segment pen object this filter should draw the results with.
- *approximateSegmentLength*: the length you want the flattened segments to be (roughly).
- *segmentLines*: whether to cut straight lines into segments as well.
- *filterDoubles*: don’t draw if a segment goes to the same coordinate.

## class ThresholdPen(otherPen, threshold=10)

This pen only draws segments longer in length than the threshold value.

- *otherPen*: a different segment pen object this filter should draw the results with.
- *threshold*: the minimum length of a segment

## flattenGlyph(aGlyph, threshold=10, segmentLines=True)

Convenience function that applies the `FlattenPen` pen to a glyph. Returns a new glyph object.

## thresholdGlyph(aGlyph, threshold=10)

Convenience function that applies the `ThresholdPen` to a glyph. Returns a new glyph object (from `objectsRF.RGlyph`).
