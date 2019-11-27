def format_output(coincidence_count, accuracy_word, accuracy_text, time_work):
  accuracy_medium = (float(accuracy_word) + float(accuracy_text)) / 2
  accuracy_medium_percentage = float("{0:.2f}".format(accuracy_medium * 100))
  time_work_percentage = float("{0:.2f}".format(time_work / 300 * 100))

  return [str(int(coincidence_count)), str(int(accuracy_medium_percentage)), str(int(time_work_percentage))]

