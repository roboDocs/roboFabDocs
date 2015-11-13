adapterPens
===========

## class FabToFontToolsPenAdapter(fontToolsPen)

Class that covers up the subtle differences between `RoboFab Pens` and `FontTools Pens`. ‘Fab should eventually move to `FontTools Pens`, this class may help to make the transition smoother.

## class GuessSmoothPointPen(outPen)

Filtering `PointPen` that tries to determine whether an on-curve point should be “smooth”, ie. that it’s a “tangent” point or a “curve” point.

## class PointToSegmentPen(segmentPen, outputImpliedClosingLine=False)

Adapter class that converts the `PointPen` protocol to the `(Segment)Pen` protocol.

### addPoint(pt, segmentType=None, smooth=False, name=None, **kwargs)

Add a point to the current sub path.

### beginPath()

Start a new sub path.

### endPath()

End the current sub path.

## class SegmentToPointPen(pointPen, guessSmooth=True)

Adapter class that converts the `(Segment)Pen` protocol to the `PointPen` protocol.

## class TransformPointPen(outPen, transformation)

`PointPen` that transforms all coordinates, and passes them to another `PointPen`. It also transforms the transformation given to `addComponent()`.
