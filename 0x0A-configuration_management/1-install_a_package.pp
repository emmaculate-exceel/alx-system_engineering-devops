##install a specfic package of flask using puppet

package {'flask':
  ensure   => '2.1.0',
  provider => 'apt',
}