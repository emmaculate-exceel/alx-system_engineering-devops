#!/usr/bin/env ruby
#search for info in a message log
#a log of [sender] [reciever] [flags]

puts ARGV[0].scan(/from:[0-9]{11}|to:[0-9]{11}|flags:.\d.\d..\d.\d..\d/).join(',')
