<?php

require 'vendor/autoload.php';
use Zend\Mail\Storage\Pop3;
use Zend\Mail\Storage\Imap;
use Zend\Mail\Storage\AbstractStorage;

$login_params = [
	'host' => '127.0.0.1',
	'port' => 5051,
	'user' => '',
	'password' => ''
];

$connection = new Pop3($login_params);
$num_messages = $connection->countMessages();
print_r("Number of messages: " . $num_messages . "\n");

for ($i=0; $i<$num_messages; $i++) {

	$msg = $connection->getMessage($num_messages - $i);

}


