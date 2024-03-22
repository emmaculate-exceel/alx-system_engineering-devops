##install a specfic package of flask using puppet
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  before   => Exec['verify_flask_version'],
}