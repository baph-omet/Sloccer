import inspect

class Default(object):
	enabled = True
	extension = "default"

	whitespace = [
		" ",
		"\t",
		"\n",
		"\r"
	]

	singleLineComment = [
		"//"
	]

	multiLineCommentOpen = [
		"/*"
	]

	multiLineCommentClose = [
		"*/"
	]

	ignore = [
		"{",
		"}",
		"[",
		"]",
		"(",
		")"
	]

class Java(Default):
	enabled = True
	extension = "java"

class CSharp(Default):
	enabled = True
	extension = "cs"

class JavaScript(Default):
	enabled = True
	extension = "js"

class CPlusPlus(Default):
	enabled = True
	extension = "cpp"

class HTML(Default):
	enabled = True
	extension = "html"

	singleLineComment = []

	multiLineCommentOpen = [
		"<!--"
	]

	multiLineCommentClose = [
		"-->"
	]

class CSS(Default):
	enabled = True
	extension = "css"

	singleLineComment = []

class Python(Default):
	enabled = True
	extension = "py"

	singleLineComment = [
		"#"
	]

	multiLineCommentOpen = [
		'"""'
	]

	multiLineCommentClose = [
		'"""'
	]

class Yaml(Default):
	enabled = True
	extension = "yml"

	whitespace = [
		" ",
		"\n"
	]

	singleLineComment = [
		"#"
	]

	multiLineCommentOpen = []

	multiLineCommentClose = []

# from http://code.activestate.com/recipes/576949-find-all-subclasses-of-a-given-class/
def itersubclasses(cls, _seen=None):
    """
    itersubclasses(cls)

    Generator over all subclasses of a given class, in depth first order.

    >>> list(itersubclasses(int)) == [bool]
    True
    >>> class A(object): pass
    >>> class B(A): pass
    >>> class C(A): pass
    >>> class D(B,C): pass
    >>> class E(D): pass
    >>>
    >>> for cls in itersubclasses(A):
    ...     print(cls.__name__)
    B
    D
    E
    C
    >>> # get ALL (new-style) classes currently defined
    >>> [cls.__name__ for cls in itersubclasses(object)] #doctest: +ELLIPSIS
    ['type', ...'tuple', ...]
    """

    if not isinstance(cls, type):
        raise TypeError('itersubclasses must be called with '
                        'new-style classes, not %.100r' % cls)
    if _seen is None: _seen = set()
    try:
        subs = cls.__subclasses__()
    except TypeError: # fails only when cls is type
        subs = cls.__subclasses__(cls)
    for sub in subs:
        if sub not in _seen:
            _seen.add(sub)
            yield sub
            for sub in itersubclasses(sub, _seen):
                yield sub

def getLanguage(extension):
	for subclass in itersubclasses(Default):
		# print("  Subclass: " + str(subclass))
		if subclass.extension == extension:
			return subclass
	return Default
