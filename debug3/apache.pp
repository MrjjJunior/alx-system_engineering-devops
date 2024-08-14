# apache.pp

# Ensure the apache2 (httpd on CentOS) package is installed
package { 'apache2':
  ensure => installed,
  provider => 'apt',
}

# Ensure the service is running and enabled
service { 'apache2':
  ensure     => running,
  enable     => true,
  provider   => 'systemd',
  require    => Package['apache2'],
}
