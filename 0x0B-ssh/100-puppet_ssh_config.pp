# Client configuration file (w/ Puppet)
# Client SSH configuration file so that you can connect to a server without typing a password.
file_line { 'PasswordAuthentication_not':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
# Client SSH configuration file so that you can connect to a server using school.
file_line { 'IdentityFile_add':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}