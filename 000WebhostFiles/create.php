
<?php

$path = "DataStores/$name";

if (!mkdir($path, 0777, true)) {
    die('Error');
}

?>
