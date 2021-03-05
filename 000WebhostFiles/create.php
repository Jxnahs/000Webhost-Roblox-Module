
<?php

$name = $_GET['name'];

$path = "DataStores/$name";

if (!mkdir($path, 0777, true)) {
    die('Error');
}

?>
