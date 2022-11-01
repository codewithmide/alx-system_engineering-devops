# puppet code to fix WordPress webstack bug
exec { 'debugging fix':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin'
  }
