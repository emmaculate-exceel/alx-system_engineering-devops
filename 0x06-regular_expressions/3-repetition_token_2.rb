#!/usr/bin/env ruby
# Search for string pattern
# using Regex in Ruby

print ARGV[0].scan(/htb{1,}n/).join()
