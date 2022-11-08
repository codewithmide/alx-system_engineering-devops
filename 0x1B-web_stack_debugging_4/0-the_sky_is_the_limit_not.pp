# Sky is the limit, let's bring that limit higher
exec { 'Skylimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
  provider => shell
}
