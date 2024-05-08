#file for puppet configuration for the puppet file

exec {'fix-apache' :
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/'
}