def find_unique_words(transcript):
  # Write code beleow 💖
  """"
  Complete the function that counts the number of unique words in a phone call.
  Args:
  transcript (str): string of words
  Returns:
  number of unique words (punctuation and capitalization are ignored)
  """
  if transcript:
    char_list = list(transcript.lower().replace(" ", "x"))
    for i in range(len(char_list)):
      if ord(char_list[i]) < 97 or ord(char_list[i]) > 122:
          char_list[i] = ""
    joined = "".join(char_list)
    clean_list = joined.split("x")
    word_dict = {key:1 for key in clean_list}
    for word in clean_list:
      if word in word_dict.keys():
        word_dict[word] += 0
    return sum(word_dict.values())
  else:
    return 0

test = ""
print(find_unique_words(test))
