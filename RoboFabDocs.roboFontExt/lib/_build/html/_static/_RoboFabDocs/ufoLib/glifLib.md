glifLib
=======

Generic module for reading and writing the .glif format.

More info about the .glif format (GLyphInterchangeFormat) can be found on the [UFO website](http://unifiedfontobject.org).

The main class in this module is `GlyphSet`. It manages a set of .glif files in a folder. It offers two ways to read glyph data, and one way to write glyph data. See the class doc string for details.

## class GlyphSet(dirName, glyphNameToFileNameFunc=None, ufoFormatVersion=3)

`GlyphSet` manages a set of .glif files inside one directory.

`GlyphSet`’s constructor takes a path to an existing directory as it’s first argument. Reading glyph data can either be done through the `readGlyph()` method, or by using `GlyphSet`’s dictionary interface, where the keys are glyph names and the values are (very) simple glyph objects.

To write a glyph to the glyph set, you use the `writeGlyph()` method. The simple glyph objects returned through the `dict` interface do not support writing, they are just a convenient way to get at the glyph data.

### deleteGlyph(glyphName)

Permanently delete the glyph from the glyph set on disk. Will raise `KeyError` if the glyph is not present in the glyph set.

### getComponentReferences(glyphNames=None)

Return a dictionary that maps glyph names to lists containing the base glyph name of components in the glyph. This parses the .glif files partially, so it is a lot faster than parsing all files completely. By default this checks all glyphs, but a subset can be passed with `glyphNames`.

### getGLIF(glyphName)

Get the raw GLIF text for a given glyph name. This only works for GLIF files that are already on disk.

This method is useful in situations when the raw XML needs to be read from a glyph set for a particular glyph before fully parsing it into an object structure via the `readGlyph` method.

Internally, this method will load a GLIF the first time it is called and then cache it. The next time this method is called the GLIF will be pulled from the cache if the file’s modification time has not changed since the GLIF was cached. For memory efficiency, the cached GLIF will be purged by various other methods such as `readGlyph`.

### getImageReferences(glyphNames=None)

Return a dictionary that maps glyph names to the file name of the image referenced by the glyph. This parses the .glif files partially, so it is a lot faster than parsing all files completely. By default this checks all glyphs, but a subset can be passed with `glyphNames`.

### getReverseContents()

Return a reversed dict of self.contents, mapping file names to glyph names. This is primarily an aid for custom glyph name to file name schemes that want to make sure they don’t generate duplicate file names. The file names are converted to lowercase so we can reliably check for duplicates that only differ in case, which is important for case-insensitive file systems.

### getUnicodes(glyphNames=None)

Return a dictionary that maps glyph names to lists containing the unicode value[s] for that glyph, if any. This parses the .glif files partially, so it is a lot faster than parsing all files completely. By default this checks all glyphs, but a subset can be passed with `glyphNames`.

### glyphClass

alias of `Glyph`

### readGlyph(glyphName, glyphObject=None, pointPen=None)

Read a .glif file for `glyphName` from the glyph set. The `glyphObject` argument can be any kind of object (even `None`); the `readGlyph()` method will attempt to set the following attributes on it:

- *width*: the advance with of the glyph
- *height*: the advance height of the glyph
- *unicodes*: a list of unicode values for this glyph
- *note*: a string
- *lib*: a dictionary containing custom data
- *image*: a dictionary containing image data
- *guidelines*: a list of guideline data dictionaries

All attributes are optional, in two ways:

1. An attribute won’t be set if the .glif file doesn’t contain data for it. `glyphObject` will have to deal with default values itself.

2. If setting the attribute fails with an AttributeError (for example if the `glyphObject` attribute is read- only), `readGlyph()` will not propagate that exception, but ignore that attribute.

To retrieve outline information, you need to pass an object conforming to the `PointPen` protocol as the `pointPen` argument. This argument may be None if you don’t need the outline data.

`readGlyph()` will raise `KeyError` if the glyph is not present in the glyph set.

### rebuildContents()

Rebuild the contents dict by loading `contents.plist`.

### writeContents()

Write the contents.plist file out to disk. Call this method when you’re done writing glyphs.

### writeGlyph(glyphName, glyphObject=None, drawPointsFunc=None, formatVersion=None)

Write a .glif file for `glyphName` to the glyph set. The `glyphObject` argument can be any kind of object (even None); the `writeGlyph()` method will attempt to get the following attributes from it:

- *width*: the advance with of the glyph
- *height*: the advance height of the glyph
- *unicodes*: a list of unicode values for this glyph
- *note*: a string “lib” a dictionary containing custom data
- *image*: a dictionary containing image data
- *guidelines*: a list of guideline data dictionaries

All attributes are optional: if `glyphObject` doesn’t have the attribute, it will simply be skipped.

To write outline data to the .glif file, `writeGlyph()` needs a function (any callable object actually) that will take one argument: an object that conforms to the PointPen protocol. The function will be called by writeGlyph(); it has to call the proper PointPen methods to transfer the outline to the .glif file.

The GLIF format version will be chosen based on the `ufoFormatVersion` passed during the creation of this object. If a particular format version is desired, it can be passed with the `formatVersion` argument.

## readGlyphFromString(aString, glyphObject=None, pointPen=None, formatVersions=(1, 2))

Read .glif data from a string into a glyph object.

The `glyphObject` argument can be any kind of object (even None); the `readGlyphFromString()` method will attempt to set the following attributes on it:

- *width*: the advance with of the glyph
- *height*: the advance height of the glyph
- *unicodes*: a list of unicode values for this glyph
- *note*: a string
- *lib*: a dictionary containing custom data
- *image*: a dictionary containing image data
- *guidelines* a list of guideline data dictionaries
- *anchors*: a list of anchor data dictionaries

All attributes are optional, in two ways:

1. An attribute won’t be set if the .glif file doesn’t contain data for it. `glyphObject` will have to deal with default values itself.

2. If setting the attribute fails with an `AttributeError` (for example if the `glyphObject` attribute is read-only), `readGlyphFromString()` will not propagate that exception, but ignore that attribute.

To retrieve outline information, you need to pass an object conforming to the `PointPen` protocol as the `pointPen` argument. This argument may be `None` if you don’t need the outline data.

The `formatVersions` argument defined the GLIF format versions that are allowed to be read.

## writeGlyphToString(glyphName, glyphObject=None, drawPointsFunc=None, writer=None, formatVersion=2)

Return .glif data for a glyph as a UTF-8 encoded string. The `glyphObject` argument can be any kind of object (even `None`); the `writeGlyphToString()` method will attempt to get the following attributes from it:

- *width*: the advance width of the glyph
- *height*: the advance height of the glyph
- *unicodes*: a list of unicode values for this glyph
- *note*: a string
- *lib*: a dictionary containing custom data
- *image*: a dictionary containing image data-
- *guidelines*: a list of guideline data dictionaries
- *anchors*: a list of anchor data dictionaries

All attributes are optional: if `glyphObject` doesn’t have the attribute, it will simply be skipped.

To write outline data to the .glif file, `writeGlyphToString()` needs a function (any callable object actually) that will take one argument: an object that conforms to the `PointPen` protocol. The function will be called by `writeGlyphToString()`; it has to call the proper `PointPen` methods to transfer the outline to the .glif file.

The GLIF format version can be specified with the `formatVersion` argument.

## glyphNameToFileName(glyphName, glyphSet)

Wrapper around the `userNameToFileName` function in `filenames.py`
