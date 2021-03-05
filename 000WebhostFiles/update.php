<?php

$database = $_GET['database'];

$key = $_GET['key'];

$value = $_GET['value'];

$myfile = fopen("Datastores/$database/$key", "w");
fwrite($myfile, $value);
fclose($myfile);
echo "Updated"


?>
