#managing server using puppet

package { 'nginx':
  ensure => 'present'
}

exec { 'install':
  command  => 'sudo apt install update; sudo apt install nginx -y,
  provider => shell,
}

exec { 'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/github.com\/emmaculate-exceel\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec { 'run':
  command  => 'sudo service nginx start',
  provider => shell,
}
