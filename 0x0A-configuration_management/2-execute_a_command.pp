##execute a command using puppet
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/',
}
