filenames
=========

User name to file name conversion. This was taken from the UFO 3 spec.

## handleClash1(userName, existing=[], prefix='', suffix='')

Existing should be a case-insensitive list of all existing file names.

	prefix = ("0" * 5) + "."
	suffix = "." + ("0" * 10)
	existing = ["a" * 5]
	e = list(existing)
	handleClash1(userName="A" * 5, existing=e, prefix=prefix, suffix=suffix)

	>>> '00000.AAAAA000000000000001.0000000000'

	e = list(existing)
	e.append(prefix + "aaaaa" + "1".zfill(15) + suffix)
	handleClash1(userName="A" * 5, existing=e, prefix=prefix, suffix=suffix)

	>>> '00000.AAAAA000000000000002.0000000000'

	e = list(existing)
	e.append(prefix + "AAAAA" + "2".zfill(15) + suffix)
	handleClash1(userName="A" * 5, existing=e, prefix=prefix, suffix=suffix)

	>>> '00000.AAAAA000000000000001.0000000000'

## handleClash2(existing=[], prefix='', suffix='')

Existing should be a case-insensitive list of all existing file names.

	prefix = ("0" * 5) + "."
	suffix = "." + ("0" * 10)
	existing = [prefix + str(i) + suffix for i in range(100)]
	e = list(existing)
	handleClash2(existing=e, prefix=prefix, suffix=suffix)

	>>> '00000.100.0000000000'

	e = list(existing)
	e.remove(prefix + "1" + suffix)
	handleClash2(existing=e, prefix=prefix, suffix=suffix)

	>>> '00000.1.0000000000'

	e = list(existing)
	e.remove(prefix + "2" + suffix)
	handleClash2(existing=e, prefix=prefix, suffix=suffix)

	>>> '00000.2.0000000000'

## userNameToFileName(userName, existing=[], prefix='', suffix='')

Existing should be a case-insensitive list of all existing file names.

	userNameToFileName(u"a")

	>>> u'a'

	userNameToFileName(u"A")

	>>> u'A_'

	userNameToFileName(u"AE")

	>>> u'A_E_'

	userNameToFileName(u"Ae")

	>>> u'A_e'

	userNameToFileName(u"ae")

	>>> u'ae'

	userNameToFileName(u"aE")

	>>> u'aE_'

	userNameToFileName(u"a.alt")

	>>> u'a.alt'

	userNameToFileName(u"A.alt")

	>>> u'A_.alt'

	userNameToFileName(u"A.Alt")

	>>> u'A_.A_lt'

	userNameToFileName(u"A.aLt")

	>>> u'A_.aL_t'

	userNameToFileName(u"A.alT")

	>>> u'A_.alT_'

	userNameToFileName(u"T_H")

	>>> u'T__H_'

	userNameToFileName(u"T_h")

	>>> u'T__h'

	userNameToFileName(u"t_h")

	>>> u't_h'

	userNameToFileName(u"F_F_I")

	>>> u'F__F__I_'

	userNameToFileName(u"f_f_i")

	>>> u'f_f_i'

	userNameToFileName(u"Aacute_V.swash")

	>>> u'A_acute_V_.swash'

	userNameToFileName(u".notdef")

	>>> u'_notdef'

	userNameToFileName(u"con")

	>>> u'_con'

	userNameToFileName(u"CON")

	>>> u'C_O_N_'

	userNameToFileName(u"con.alt")

	>>> u'_con.alt'

	userNameToFileName(u"alt.con")

	>>> u'alt._con'
	