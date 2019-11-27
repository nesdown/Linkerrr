def count_coincidence(word, words_array):
  counter = 0
  for current_word in words_array:
    if (word == current_word) or (word in current_word):
      counter += 1

  return counter
