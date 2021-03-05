<?php

$database = $_GET['database'];

$key = $_GET['key'];

$filename = "Datastores/$database/$key";
if (file_exists($filename)) {
    $handle = fopen($filename, "r");
    $contents = fread($handle, filesize($filename));
    echo $contents;
    fclose($handle);
} else {
    echo "No data";
}
?>
