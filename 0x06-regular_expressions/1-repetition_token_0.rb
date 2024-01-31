#!/usr/bin/env ruby
#search for htb using regex

print ARGV[0].scan(/hbt{2,5}n/).join()
