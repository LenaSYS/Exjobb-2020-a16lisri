<?php 

//Establish MongoDB Connection:
$m = new MongoDB\Driver\Manager("mongodb://admin:admin123@localhost:27017");
echo "Connection to database successfull.";

//Prepare file for writing:
$OutputtoTextfile = fopen("query1_mongodb.csv", 'a') or die("Unable to open file!");

//Prepare your variable for your array here:
$time[] = ""; 
$totalexecution = "0";
 
// Start loop 
for($i = 1; $i <=1000; $i++) 
{
    // Starting clock time in seconds - start inside loop to monitor transaction instance not the overall transaction time
        $start_time = microtime(true);
    // Query	
	$command = new MongoDB\Driver\Command([
   	    'aggregate' => 'business_data',
    	    'pipeline' => [
        	['$group' => ['_id' => 'null', 'total' => ['$sum' => '$Data_value']]],
    	    ],
    	    'cursor' => new stdClass,
]);
$cursor = $m->executeCommand('mymongodb', $command);

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
