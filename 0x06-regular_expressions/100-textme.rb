#!/usr/bin/env ruby
#search for info in a message log
#a log of [sender] [reciever] [flag]

from = ARGV[0].scan(/from:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts [from, to, flags].join(',')
