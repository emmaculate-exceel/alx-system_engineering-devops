#!/usr/bin/env ruby
# searching for phone numbers

puts ARGV[0].scan(/^[0-9]{10}$/).join()
