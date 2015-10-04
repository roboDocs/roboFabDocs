# build RoboFab Docs as a RoboFont Extension

import os
from mojo.extensions import ExtensionBundle

libPath = os.path.dirname(__file__)
extensionFolder = os.path.join(libPath, 'extension')
extensionFile = "RoboFabDocs.roboFontExt"
extensionPath = os.path.join(extensionFolder, extensionFile)
extensionHtml = os.path.join(os.path.dirname(libPath), "Docs/build/html/")

print "building RoboFab Docs extension...",

B = ExtensionBundle()
B.name = "RoboFab Docs"
B.developer = "RoboFab Developers"
B.developerURL = "http://robofab.org/"
B.version = "0.1"
B.mainScript = ""
B.launchAtStartUp = 0
B.addToMenu = [{"path" : "docs.py", "preferredName" : "RoboFab Docs", "shortKey" : ""}]
B.requiresVersionMajor = "1"
B.requiresVersionMinor = "5"
B.infoDictionary["html"] = 0
B.infoDictionary["com.robofontmechanic.Mechanic"] = {"repository" : "roboDocs/roboFabDocsExtension"}
B.save(extensionPath, libPath=libPath, resourcesPath=None, pycOnly=False)

print "done."
