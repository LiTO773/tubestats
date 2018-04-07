import HTMLParser
import json
import os

# Process subtitle file (get word count)
# TODO Use HTMLParser to parse ttml properly
def handle_file(file):
  for i in range(len(file)):
    new_line = file[i][54:-5].decode('utf-8', 'ignore')
    new_line = new_line.replace('</span>', '')
    new_line = new_line.replace('<span style="s1">', '')
    new_line = new_line.replace('<span style="s2">', '')
    new_line = new_line.replace('<span style="s3">', '')
    new_line = new_line.replace('<span style="s4">', '')
    new_line = html_parser.unescape(new_line).lower()
    new_line = new_line.strip().split(' ')
    file[i] = new_line
  return file


def flat(word_matrix):
  # Flat word list
  word_list = []
  for word_arr in word_matrix:
    word_list.extend(word_arr)
  return word_list

# Creates a map with all the words and their count
def create_write_map(word_list):
  count_map = {}
  
  for word in word_list:
    if word not in count_map:
      count_map[word] = 1
    else:
      count_map[word] += 1

  # Write a report
  f = open('foo.json', 'w+')
  f.write(json.dumps(count_map, indent=4, sort_keys=True))
  f.close()


words = []
for file in os.listdir('examples'):
  # Get the subtitles files
  # TODO Get the file name as an argument
  html_parser = HTMLParser.HTMLParser()
  subtitle_file = open('./examples/' + file)
  cut_file = subtitle_file.readlines()[15:-3]
  word_matrix = handle_file(cut_file)
  words.append(flat(word_matrix))

# Creates the channel word and count map
words = flat(words)
create_write_map(words)

