def update_dictionary(a_dictionary, key, value):
  """Replaces or adds key/value in a dictionary."""

  if key in a_dictionary:
    a_dictionary[key] = value
  else:
    a_dictionary[key] = value

  return a_dictionary