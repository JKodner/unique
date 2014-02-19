def unique(seq):
	"""Returns a sequence (of the same input type) containing all unique elements.
	If an inappropriate sequence is inputed (neither a list or tuple), an error is raised."""
	if isinstance(seq, list):
		new_seq = []
		for i in seq:
			if i not in new_seq:
				new_seq.append(i)
	elif isinstance(seq, tuple):
		new_seq = ()
		for i in seq:
			if i not in new_seq:
				new_seq += (i,)
	else:
		raise ValueError ("Inappropriate Sequence: Must be List or Tuple.")
	return new_seq