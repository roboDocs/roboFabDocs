objectsBase
===========

These are base classes for `Font`, `Glyph`, `Contour`, `Segment` and `Point` objects. This defines the basic API that needs to be supported in RoboFab objects.

<a name='BaseAnchor'></a>
## class BaseAnchor

Base class for all anchor point objects.

### copy(aParent=None)

Duplicate this anchor.

### draw(pen)

Draw the object onto a segment pen

### drawPoints(pen)

draw the object with a point pen

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### move((x, y))

Move the anchor

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

round the values in the anchor

### scale((x, y), center=(0, 0))

scale the anchor

### transform(matrix)

Transform this anchor. Use a Transform matrix object from `fontTools.misc.transform`

<a name='BaseBPoint'></a>
## class BaseBPoint

Base class for `bPoints` objects.

### anchor

the position of the anchor

### bcpIn

the `(x,y)` for the incoming bcp

### bcpOut

the `(x,y)` for the outgoing bcp

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### move((x, y))

move the `bPoint`

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

Round the coordinates to integers

### scale((x, y), center=(0, 0))

scale the `bPoint`

### select(state=True)

Set the selection of this point. 

**This method should be a lot more versatile, dealing with different kinds of selection, select the bcp’s seperately etc. But that’s for later when we need it more. For now it’s just one flag for the entire thing.**

### transform(matrix)

Transform this point. Use a Transform matrix object from `fontTools.misc.transform`

### type

the type of bPoint, either ‘corner’ or ‘curve’

<a name='BaseComponent'></a>
## class BaseComponent

Base class for all component objects.

### box

the bounding box of the component: `(xMin, yMin, xMax, yMax)`

### copy(aParent=None)

Duplicate this component.

### draw(pen)

Segment pen drawing method.

### drawPoints(pen)

draw the object with a point pen

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

round the offset values

<a name='BaseContour'></a>
## class BaseContour

Base class for all contour objects.

### appendBPoint(pointType, anchor, bcpIn=(0, 0), bcpOut=(0, 0))

append a bPoint to the contour

### autoStartSegment()

automatically set the lower left point of the contour as the first point.

### box

the bounding box for the contour

### clockwise

direction of contour: `1=clockwise 0=counterclockwise`

### copy(aParent=None)

Duplicate this contour

### draw(pen)

draw the object with a fontTools pen

### drawPoints(pen)

draw the object with a point pen

### getParent()

this method will be overwritten with a weakref if there is a parent.

### insertBPoint(index, pointType, anchor, bcpIn=(0, 0), bcpOut=(0, 0))

insert a bPoint at index on the contour

### isRobofab()

Presence of this method indicates a Robofab object

### move((x, y))

move the contour

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### pointInside((x, y), evenOdd=0)

determine if the point is inside or ouside of the contour

### rotate(angle, offset=None)

rotate the contour

### round()

round the value of all points in the contour

### scale((x, y), center=(0, 0))

scale the contour

### skew(angle, offset=None)

skew the contour

### transform(matrix)

Transform this contour. Use a Transform matrix object from `robofab.transform`

<a name='BaseFont'></a>
## class BaseFont

Base class for all font objects.

### autoUnicodes()

Using fontTools.agl, assign Unicode lists to all glyphs in the font

### close(save=1)

Close the font, saving is optional.

### compileGlyph(glyphName, baseName, accentNames, adjustWidth=False, preflight=False, printErrors=True)

Compile components into a new glyph using components and anchorpoints.  

- *glyphName*: the name of the glyph where it all needs to go  
- *baseName*: the name of the base glyph  
- *accentNames*: a list of *accentName*, *anchorName* tuples, `[(‘acute’, ‘top’), etc]`

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### generateGlyph(glyphName, replace=1, preflight=False, printErrors=True)

Generate a glyph and return it. Assembled from `GlyphConstruction.txt`

### getCharacterMapping()

Create a dictionary of unicode -> [glyphname, ...] mappings. Note that this dict is created each time this method is called, which can make it expensive for larger fonts. All glyphs are loaded. Note that one glyph can have multiple unicode values, and a unicode value can have multiple glyphs pointing to it.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### getReverseComponentMapping()

Get a reversed map of component references in the font. `{ ‘A’ : [‘Aacute’, ‘Aring’] ‘acute’ : [‘Aacute’] ‘ring’ : [‘Aring’] etc. }`

### interpolate(factor, minFont, maxFont, suppressError=True, analyzeOnly=False, doProgress=False)

Traditional interpolation method. Interpolates by factor between `minFont` and `maxFont`. `suppressError` will supress all tracebacks and analyze only will not perform the interpolation but it will analyze all glyphs and return a dict of problems.

### isRobofab()

Presence of this method indicates a Robofab object

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

round all of the points in all of the glyphs

### update()

update the font

<a name='BaseGlyph'></a>
## class BaseGlyph

Base class for all glyph objects.

### appendContour(aContour, offset=(0, 0))

append a contour to the glyph

### appendGlyph(aGlyph, offset=(0, 0))

append another glyph to the glyph

### autoContourOrder()

attempt to sort the contours based on their centers

### autoUnicodes()

Using `fontTools.agl`, assign Unicode list to the glyph

### box

the bounding box of the glyph: (xMin, yMin, xMax, yMax)

### copy(aParent=None)

Duplicate this glyph

### correctDirection(trueType=False)

corect the direction of the contours in the glyph.

### draw(pen)

draw the object with a RoboFab segment pen

### drawPoints(pen)

draw the object with a point pen

### getGlyph(glyphName)

Provided there is a font parent for this glyph, return a sibling glyph.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### getPen()

Return a Pen object for creating an outline in this glyph.

### getPointPen()

Return a PointPen object for creating an outline in this glyph.

### interpolate(factor, minGlyph, maxGlyph, suppressError=True, analyzeOnly=False)

Traditional interpolation method. Interpolates by factor between `minGlyph` and `maxGlyph`. `suppressError` will supress all tracebacks and analyze only will not perform the interpolation but it will analyze all glyphs and return a dict of problems.

### isCompatible(otherGlyph, report=True)

Return a bool value if the glyph is compatible with *otherGlyph*. With `report=True`, `isCompatible` will return a report of what’s wrong. The interpolate method requires absolute equality between contour data. Absolute equality is preferred among component and anchor data, but it is **not** required. Interpolation between components and anchors will only deal with compatible data and incompatible data will be ignored. This method reflects this system.

### isEmpty()

return true if the glyph has no contours or components

### isRobofab()

Presence of this method indicates a Robofab object

### leftMargin

the left margin

### move((x, y), contours=True, components=True, anchors=True)

Move a glyph’s items that are flagged as True

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### pointInside((x, y), evenOdd=0)

determine if the point is in the black or white of the glyph

### rightMargin

the right margin

### rotate(angle, offset=None)

rotate the glyph

### round()

round all coordinates in all contours, components and anchors

### scale((x, y), center=(0, 0))

scale the glyph

### skew(angle, offset=None)

skew the glyph

### transform(matrix)

Transform this glyph. Use a Transform matrix object from `robofab.transform`

### update()

update the glyph

<a name='BaseGroups'></a>
## class BaseGroups

Base class for all RFont.groups objects

### clear()

→ None. Remove all items from D.

### copy()

→ a shallow copy of D

### findGlyph(glyphName)

return a list of all groups contianing glyphName

### static fromkeys(S[, v])

→ New dict with keys from S and values equal to v.
v defaults to None.

### get(k[, d])

→ `D[k] if k in D, else d`. d defaults to None.

### getParent()

this method will be overwritten with a *weakref* if there is a parent.

### has_key(k)

→ `True if D has a key k, else False`

### items()

→ list of D's `(key, value)` pairs, as 2-tuples

### iteritems()

→ an iterator over the `(key, value)` items of D

### iterkeys()

→ an iterator over the keys of D

### itervalues()

→ an iterator over the values of D

### keys()

→ list of D's keys

### pop(k[, d])

→ v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise `KeyError` is raised

### popitem()

→ (k, v), remove and return some (key, value) pair as a 2-tuple; but raise `KeyError` if D is empty.

### setdefault(k[, d])

→ `D.get(k,d)`, also set `D[k]=d if k not in D`

### update(E, **F)

→ None. Update `D` from dict/iterable `E` and `F`.

If `E` has a `.keys()` method, does: `for k in E: D[k] = E[k]`. If `E` lacks `.keys()` method, does: `for (k, v) in E: D[k] = v`.

In either case, this is followed by: `for k in F: D[k] = F[k]`

### values()

→ list of D's values

<a name='BaseGuide'></a>
## class BaseGuide

Base class for all guide objects.

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

Placeholder. Round all numerical values.

<a name='BaseKerning'></a>
## class BaseKerning(kerningDict=None)

Base class for all kerning objects. Object behaves like a dict but has some special kerning specific tricks.

### add(value)

add value to all kerning pairs

### asDict(returnIntegers=True)

return the object as a dictionary

### clear()

clear all kerning

### combine(kerningDicts, overwriteExisting=True)

combine two or more kerning dictionaries. overwrite existing duplicate pairs if `overwriteExisting=True`

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### eliminate(leftGlyphsToEliminate=None, rightGlyphsToEliminate=None, analyzeOnly=False)

eliminate pairs containing a left glyph that is in the `leftGlyphsToEliminate` list or a right glyph that is in the `rightGlyphsToELiminate` list. `sideGlyphsToEliminate` can be a string: `'a'` or list: `['a, 'b']`.

`analyzeOnly` will not remove pairs. it will return a count of all pairs that would be removed.

### explodeClasses(leftClassDict=None, rightClassDict=None, analyzeOnly=False)

turn class kerns into real kerning pairs. classes should be defined in dicts: `{‘O’:[‘C’, ‘G’, ‘Q’], ‘H’:[‘B’, ‘D’, ‘E’, ‘F’, ‘I’]}`. 

`analyzeOnly` will not remove pairs. it will return a count of all pairs that would be added

### get(pair, default=None)

get a value. return None if the pair does not exist

### getAverage()

return average of all kerning pairs

### getExtremes()

return the lowest and highest kerning values

### getLeft(glyphName)

Return a list of kerns with glyphName as left character.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### getRight(glyphName)

Return a list of kerns with glyphName as left character.

### implodeClasses(leftClassDict=None, rightClassDict=None, analyzeOnly=False)

condense the number of kerning pairs by applying classes. this will eliminate all pairs containg the classed glyphs leaving pairs that contain the key glyphs behind. `analyzeOnly` will not remove pairs. it will return a count of all pairs that would be removed.

### importAFM(path, clearExisting=True)

Import kerning pairs from an AFM file. clearExisting=True will clear all exising kerning

### interpolate(sourceDictOne, sourceDictTwo, value, clearExisting=True)

interpolate the kerning between `sourceDictOne` and `sourceDictTwo`. clearExisting will clear existing kerning first.

### isRobofab()

Presence of this method indicates a Robofab object

### items()

return a list of kerning items

### keys()

return list of kerning pairs

### minimize(minimum=10)[source

eliminate pairs with value less than minimum

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### occurrenceCount(glyphsToCount)

return a dict with glyphs as keys and the number of occurances of that glyph in the kerning pairs as the value `glyphsToCount` can be a string: `'a'` or list: `[‘a’, ‘b’]`

### remove(pair)

remove a kerning pair

### round(multiple=10)

round the kerning pair values to increments of multiple

### scale(value)

scale all kernng pairs by value

### swapNames(swapTable)

change glyph names in all kerning pairs based on swapTable. `swapTable = {‘BeforeName’:’AfterName’, ...}`

### update(kerningDict)

replace kerning data with the data in the given kerningDict

### values()

return a list of kerning values

<a name='BaseLib'></a>
## class BaseLib

Base class for all lib objects

### clear()

→ None. Remove all items from D.

### copy(aParent=None)

Duplicate this lib.

### static fromkeys(S[, v])

→ New dict with keys from S and values equal to v.
v defaults to None.

### get(k[, d])

→ D[k] if k in D, else d. d defaults to None.
getParent()[source]
this method will be overwritten with a weakref if there is a parent.

### has_key(k)

→ True if D has a key k, else False

### items()

→ list of D's (key, value) pairs, as 2-tuples

### iteritems()

→ an iterator over the (key, value) items of D

### iterkeys()

→ an iterator over the keys of D

### itervalues()

→ an iterator over the values of D

### keys()

→ list of D's keys

### pop(k[, d])

→ v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised

### popitem()

→ `(k, v)`, remove and return some `(key, value)` pair as a 2-tuple; but raise `KeyError` if D is empty.

### setdefault(k[, d])

→ `D.get(k,d)`, also set `D[k]=d if k not in D update(E, **F)`

→ None. Update D from dict/iterable E and F.

If E has a .keys() method, does: for k in E: D[k] = E[k] If E lacks .keys() method, does: for (k, v) in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

### values()

→ list of D's values

<a name='BasePoint'></a>
## class BasePoint

Base class for point objects.

### copy(aParent=None)

Duplicate this point

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### move((x, y))

Move the point

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

round the values in the point

### scale((x, y), center=(0, 0))

scale the point

### select(state=True)

Set the selection of this point.

**This method should be a lot more versatile, dealing with different kinds of selection, select the bcp’s seperately etc. But that’s for later when we need it more. For now it’s just one flag for the entire thing.**

### transform(matrix)

Transform this point. Use a Transform matrix object from fontTools.misc.transform

### class robofab.objects.objectsBase.BasePostScriptFontHintValues(data=None)

Base class for font-level postscript hinting information. Blues values, stem values.

### clear()

Set all attributes to default / empty

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isEmpty()

Check all attrs and decide if they’re all empty.

### round()

Round the values to reasonable values. - blueScale is not rounded, it is a float - forceBold is set to False if -0.5 < value < 0.5. Otherwise it will be True. - blueShift, blueFuzz are rounded to int - stems are rounded to int - blues are rounded to int

<a name='BasePostScriptGlyphHintValues'></a>
## class BasePostScriptGlyphHintValues(data=None)

Base class for glyph-level postscript hinting information. vStems, hStems

### clear()

Set all attributes to default / empty

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isEmpty()

Check all attrs and decide if they’re all empty.

### round()

Round the values to reasonable values. - stems are rounded to int

<a name='BasePostScriptHintValues'></a>
## class BasePostScriptHintValues(data=None)

Base class for postscript hinting information.

### clear()

Set all attributes to default / empty

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isEmpty()[source]

Check all attrs and decide if they’re all empty.

<a name='BaseSegment'></a>
## class robofab.objects.objectsBase.BaseSegment

Base class for all segment objects

### copy(aParent=None)[source]

Duplicate this segment

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### move((x, y))

move the segment

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### offCurve

on curve point for the segment

### onCurve

list of off curve points for the segment

### round()

round all points in the segment

### scale((x, y), center=(0, 0))

scale the segment

### transform(matrix)

Transform this segment. Use a Transform matrix object from robofab.transform

<a name='FuzzyNumber'></a>
## class FuzzyNumber(value, threshold)

Number-like object that will match another fuzzy number if the values are within a specific range.

<a name='RBaseObject'></a>
## class RBaseObject

Base class for wrapper objects

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### isRobofab()

Presence of this method indicates a Robofab object

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### round()

Placeholder. Round all numerical values.

## absoluteBCPIn(anchor, BCPIn)

Convert relative incoming bcp value to an absolute value 

**Note: How is this different from absoluteBCPOut?**

## robofab.objects.objectsBase.absoluteBCPOut(anchor, BCPOut)

Convert relative outgoing bcp value to an absolute value

## robofab.objects.objectsBase.addPt(ptA, ptB)

Add two vectors

## robofab.objects.objectsBase.issequence(x)

Is *x* a sequence? We say it is if it has a `__getitem__` method.

## robofab.objects.objectsBase.mulPt(ptA, scalar)

Multiply a vector with scalar

## robofab.objects.objectsBase.relativeBCPIn(anchor, BCPIn)

Convert absolute incoming bcp value to a relative value.

**Note: How is this different from relativeBCPOut?**

## robofab.objects.objectsBase.relativeBCPOut(anchor, BCPOut)

Convert absolute outgoing bcp value to a relative value

## robofab.objects.objectsBase.roundPt((x, y))

Round a vector

## robofab.objects.objectsBase.subPt(ptA, ptB)

Substract two vectors
