#!/usr/bin/env ruby
#Regex to search for htb+ pattern

print ARGV[0].scan(/hb?tn/).join()
