<?php

//Establish MySQL Connection:
    $server = "localhost";
    $username = "a16lisri";
    $password = "123!";
    $database = "mymysql";
    $mysqli = new mysqli($server, $username, $password, $database);

//Prepare file for writing:
$OutputtoTextfile = fopen("query3_mysql.csv", 'a') or die("Unable to open file!");

//Prepare your variable for your array here:
$time[] = "";
$totalexecution = "0";

// Start loop
for($i = 1; $i <=1000; $i++)
{
    // Starting clock time in seconds - start inside loop to monitor transaction instance not the overall transaction time
        $start_time = microtime(true);
        $query="select Data_value, Period from business";
        $mysqli->query("$query");
    // End clock time in seconds
        $end_time = microtime(true);
    // Calculate script execution time
        $execution_time = ($end_time - $start_time);
    // Add to total Execution time if we want to monitor that
        $totalexecution = $totalexecution + $execution_time;
    // Write Execution time into array after this line:
    echo $i . "," . $execution_time . ",";
    $txt = $i . "," . $execution_time . ",";
    fwrite($OutputtoTextfile, $txt);
};

fclose($OutputtoTextfile);

$mysqli->close();
echo "Total Execution time of script = ".$totalexecution." sec";
?>
