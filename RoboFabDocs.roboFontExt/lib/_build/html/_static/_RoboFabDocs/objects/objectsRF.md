objectsRF
=========

This is the new doc for the `objectsRF` module.

## CurrentFont()

`CurrentFont` is not available in `objectsRF`.

## CurrentGlyph()

`CurrentGlyph` is not available in `objectsRF`.

## OpenFont(path=None, note=None)

Open a font from a path. If path is not given, present the user with a dialog (availability of dialogs will vary)

## class RFont(path=None)

Font object representing the data in an UFO.

`myFontInstace[‘A’]` access the font as a dictionary with glyphnames as key

### autoUnicodes()

Using `fontTools.agl`, assign Unicode lists to all glyphs in the font

### close(save=1)

Close the font, saving is optional.

### compileGlyph(glyphName, baseName, accentNames, adjustWidth=False, preflight=False, printErrors=True)

Compile components into a new glyph using components and anchorpoints.

*glyphName*: the name of the glyph where it all needs to go  
*baseName*: the name of the base glyph  
*accentNames*: a list of *accentName*, *anchorName* tuples, `[(‘acute’, ‘top’), etc]`  

### copy(aParent=None)

Duplicate this object. Pass an object for parenting if you want.

### generateGlyph(glyphName, replace=1, preflight=False, printErrors=True)

Generate a glyph and return it. Assembled from GlyphConstruction.txt

### getCharacterMapping()

Create a dictionary of `unicode -> [glyphname, ...]` mappings. Note that this dict is created each time this method is called, which can make it expensive for larger fonts. All glyphs are loaded. Note that one glyph can have multiple unicode values, and a unicode value can have multiple glyphs pointing to it.

### getParent()

this method will be overwritten with a weakref if there is a parent.

### getReverseComponentMapping()

Get a reversed map of component references in the font.

    { ‘A’ : [‘Aacute’, ‘Aring’] ‘acute’ : [‘Aacute’] ‘ring’ : [‘Aring’] etc. }

### insertGlyph(glyph, name=None)

returns a new glyph that has been inserted into the font

### interpolate(factor, minFont, maxFont, suppressError=True, analyzeOnly=False, doProgress=False)

Traditional interpolation method. Interpolates by factor between minFont and maxFont. `suppressError` will supress all tracebacks and analyze only will not perform the interpolation but it will analyze all glyphs and return a dict of problems.

### isRobofab()

Presence of this method indicates a Robofab object

### naked()

Return the wrapped object itself, in case it is needed for direct access.

### newGlyph(glyphName, clear=True)

Make a new glyph with glyphName if the glyph exists and `clear=True` clear the glyph

### path

path of the font

### removeGlyph(glyphName)

remove a glyph from the font

### round()

round all of the points in all of the glyphs

### save(destDir=None, doProgress=False, formatVersion=2)

Save the Font in UFO format.

### update()

update the font
