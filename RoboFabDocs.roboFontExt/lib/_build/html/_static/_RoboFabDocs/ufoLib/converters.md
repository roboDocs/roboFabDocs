converters
==========

Conversion functions.

## test()

	testKerning = {
		"A" : {
			"A" : 1,
			"B" : 2,
			"CGroup" : 3,
			"DGroup" : 4
		},
		"BGroup" : {
			"A" : 5,	
			"B" : 6,
			"CGroup" : 7,
			"DGroup" : 8
		},
		"CGroup" : {
			"A" : 9,
			"B" : 10,
			"CGroup" : 11,
			"DGroup" : 12
		},
	}

	testGroups = {
		"BGroup" : ["B"],
		"CGroup" : ["C"],
		"DGroup" : ["D"],
	}

	kerning, groups = convertUFO1OrUFO2KerningToUFO3Kerning(testKerning, testGroups)

	expected = {
		"A" : {
			"A": 1,
			"B": 2,
			"public.kern2.CGroup": 3,
			"public.kern2.DGroup": 4
		},
		"public.kern1.BGroup": {
			"A": 5,
			"B": 6,
			"public.kern2.CGroup": 7,
			"public.kern2.DGroup": 8
		},
		"public.kern1.CGroup": {
			"A": 9,
			"B": 10,
			"public.kern2.CGroup": 11,
			"public.kern2.DGroup": 12
		}
	}

	print kerning == expected

	>>> True

	expected = {
		"BGroup": ["B"],
		"CGroup": ["C"],
		"DGroup": ["D"],
		"public.kern1.BGroup": ["B"],
		"public.kern1.CGroup": ["C"],
		"public.kern2.CGroup": ["C"],
		"public.kern2.DGroup": ["D"],
	}

	print groups == expected

	>>> True
