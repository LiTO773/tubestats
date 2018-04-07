import HTMLParser
import json
# Get the subtitles files
# TODO Get the file name as an argument
html_parser = HTMLParser.HTMLParser()
subtitle_file = open('./examples/00001.en.ttml')
cut_file = subtitle_file.readlines()[15:-3]

# Process subtitle file (get word count)
# TODO Use HTMLParser to parse ttml properly
for i in range(len(cut_file)):
  new_line = cut_file[i][54:-5].decode('utf-8', 'ignore')
  new_line = new_line.replace('</span>', '')
  new_line = new_line.replace('<span style="s1">', '')
  new_line = new_line.replace('<span style="s2">', '')
  new_line = new_line.replace('<span style="s3">', '')
  new_line = new_line.replace('<span style="s4">', '')
  new_line = html_parser.unescape(new_line).lower()
  new_line = new_line.strip().split(' ')
  cut_file[i] = new_line

# Flat word list
word_list = []
for word_arr in cut_file:
  word_list.extend(word_arr)

# Creates a map with all the words and their count
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