ufoLib
======

A library for importing .ufo files and their descendants. Refer to [unifiedfontobject.com](http://unifiedfontobject.com) for the UFO specification.

The `UFOReader` and `UFOWriter` classes support versions 1 and 2 of the specification. Up and down conversion functions are also supplied in this library. These conversion functions are only necessary if conversion without loading the UFO data into a set of objects is desired. These functions are:

-  `convertUFOFormatVersion1ToFormatVersion2`

Two sets that list the font info attribute names for the two fontinfo.plist formats are available for external use. These are:

- `fontInfoAttributesVersion1`
- `fontInfoAttributesVersion2`

A set listing the `fontinfo.plist` attributes that were deprecated in version 2 is available for external use:

- `deprecatedFontInfoAttributesVersion2`

A function, `validateFontInfoVersion2ValueForAttribute`, that does some basic validation on values for a `fontinfo.plist` value is available for external use.

Two value conversion functions are availble for converting `fontinfo.plist` values between the possible format versions.

- `convertFontInfoValueForAttributeFromVersion1ToVersion2`
- `convertFontInfoValueForAttributeFromVersion2ToVersion1`

## class UFOReader(path)

Read the various components of the .ufo.

### formatVersion

The format version of the UFO. This is determined by reading `metainfo.plist` during `__init__`.

### getCharacterMapping(layerName=None)

Return a dictionary that maps unicode values (`int`s) to lists of glyph names.

### getDataDirectoryListing(maxDepth=100)

Returns a list of all files in the data directory. The returned paths will be relative to the UFO. This will not list directory names, only file names. Thus, empty directories will be skipped.

The `maxDepth` argument sets the maximum number of sub-directories that are allowed.

### getDefaultLayerName()

Get the default layer name from `layercontents.plist`.

### getGlyphSet(layerName=None)

Return the `GlyphSet` associated with the glyphs directory mapped to `layerName` in the UFO. If `layerName` is not provided, the name retrieved with `getDefaultLayerName` will be used.

### getImageDirectoryListing()

Returns a list of all image file names in the images directory. Each of the images will have been verified to have the PNG signature.

### getLayerNames()

Get the ordered layer names from `layercontents.plist`.

### getReadFileForPath(path, encoding=None)

Returns a file (or file-like) object for the file at the given `path`. The `path` must be relative to the UFO path. Returns `None` if the file does not exist. An encoding may be passed if needed.

Note: The caller is responsible for closing the open file.

### readBytesFromPath(path, encoding=None)

Returns the bytes in the file at the given `path`. The `path` must be relative to the UFO path. Returns `None` if the file does not exist. An encoding may be passed if needed.

### readFeatures()

Read `features.fea`. Returns a `string`.

### readGroups()

Read `groups.plist`. Returns a `dict`.

### readImage(fileName)

Return image data for the file named `fileName`.

### readInfo(info)

Read `fontinfo.plist`. It requires an object that allows setting attributes with names that follow the `fontinfo.plist` version 3 specification. This will write the attributes defined in the file into the object.

### readKerning()

Read `kerning.plist`. Returns a `dict`.

### readLib()

Read `lib.plist`. Returns a `dict`.

### readMetaInfo()

Read `metainfo.plist`. Only used for internal operations.

## class UFOWriter(path, formatVersion=3, fileCreator='org.robofab.ufoLib')

Write the various components of the .ufo.

### copyFromReader(reader, sourcePath, destPath)

Copy the `sourcePath` in the provided `UFOReader` to `destPath` in this writer. The paths must be relative. They may represent directories or paths. This uses the most memory efficient method possible for copying the data possible.

### copyImageFromReader(reader, sourceFileName, destFileName)

Copy the `sourceFileName` in the provided `UFOReader` to `destFileName` in this writer. This uses the most memory efficient method possible for copying the data possible.

### deleteGlyphSet(layerName)

Remove the glyph set matching `layerName`.

### fileCreator

The file creator of the UFO. This is set into `metainfo.plist` during `__init__`.

### formatVersion

The format version of the UFO. This is set into `metainfo.plist` during `__init__`.

### getFileObjectForPath(path, encoding=None)

Creates a write mode file object at `path`. If needed, the directory tree for the given path will be built. The `path` must be relative to the UFO. An encoding may be passed if needed.

Note: The caller is responsible for closing the open file.

### getGlyphSet(layerName=None, defaultLayer=True, glyphNameToFileNameFunc=None)

Return the `GlyphSet` object associated with the appropriate glyph directory in the .ufo. If `layerName` is None, the default glyph set will be used. The `defaultLayer` flag indictes that the layer should be saved into the default glyphs directory.

### removeFileForPath(path)

Remove the file (or directory) at path. The path must be relative to the UFO. This is only allowed for files in the data and image directories.

### removeImage(fileName)

Remove the file named fileName from the images directory.

### renameGlyphSet(layerName, newLayerName, defaultLayer=False)

Rename a glyph set.

Note: if a `GlyphSet` object has already been retrieved for `layerName`, it is up to the caller to inform that object that the directory it represents has changed.

### writeBytesToPath(path, bytes, encoding=None)

Write `bytes` to `path`. If needed, the directory tree for the given `path` will be built. The `path` must be relative to the UFO. An encoding may be passed if needed.

### writeFeatures(features)

Write `features.fea`. This method requires a features string as an argument.

### writeGroups(groups)

Write `groups.plist`. This method requires a `dict` of glyph groups as an argument.

### writeImage(fileName, data)

Write data to `fileName` in the images directory. The data must be a valid PNG.

### writeInfo(info)

Write `info.plist`. This method requires an object that supports getting attributes that follow the `fontinfo.plist` version 2 specification. Attributes will be taken from the given object and written into the file.

### writeKerning(kerning)

Write `kerning.plist`. This method requires a `dict` of kerning pairs as an argument.

### writeLayerContents(layerOrder=None)

Write the `layercontents.plist` file. This method must be called after all glyph sets have been written.

### writeLib(libDict)

Write `lib.plist`. This method requires a lib `dict` as an argument.

## convertUFOFormatVersion1ToFormatVersion2(inPath, outPath=None)

Function for converting a version format 1 UFO to version format 2. `inPath` should be a path to a UFO. `outPath` is the path where the new UFO should be written. If `outPath` is not given, the inPath will be used and, therefore, the UFO will be converted in place. Otherwise, if `outPath` is specified, nothing must exist at that path.

## validateFontInfoVersion2ValueForAttribute(attr, value)

This performs very basic validation of the value for attribute following the UFO 2 `fontinfo.plist` specification. The results of this should not be interpretted as correct for the font that they are part of. This merely indicates that the value is of the proper type and, where the specification defines a set range of possible values for an attribute, that the value is in the accepted range.

## convertFontInfoValueForAttributeFromVersion1ToVersion2(attr, value)

Convert value from version 1 to version 2 format. Returns the new attribute name and the converted value. If the value is `None`, `None` will be returned for the new value.

## convertFontInfoValueForAttributeFromVersion2ToVersion1(attr, value)

Convert value from version 2 to version 1 format. Returns the new attribute name and the converted value. If the value is `None`, `None` will be returned for the new value.
