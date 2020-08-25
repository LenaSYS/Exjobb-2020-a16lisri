<?php 

//Establish MongoDB Connection:
$m = new MongoDB\Driver\Manager("mongodb://admin:admin123@localhost:27017");

//Prepare file for writing:
$OutputtoTextfile = fopen("baseline_mongodb_100.csv", 'a') or die("Unable to open file!");

//Prepare your variable for your array here:
$totalexecution = "0";
 
// Start loop 
for($i = 1; $i <=100; $i++) 
{
    // Starting clock time in seconds - start inside loop to monitor transaction instance not the overall transaction time
        $start_time = microtime(true);
    // Query	
	$filter = ['Data_value' => ['$gt' => 3500]];

	$query = new MongoDB\Driver\Query($filter);
	$cursor = $m->executeQuery('mymongodb.business_data', $query);

	foreach ($cursor as $document) {
    	var_dump($document);
}

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

echo "Total Execution time of script = ".$totalexecution." sec";
?>
