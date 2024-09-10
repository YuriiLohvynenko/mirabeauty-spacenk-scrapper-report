<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Average product price sorted by highest price</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Brand</th>
        <th>Average product price</th>
      </tr>
    </thead>
    


<?php

function real_value($value) {
  $return_value = str_replace("@@@", "'", $value);
  return $return_value;
}

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mirabeauty_scraper";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT `brand`, Round(AVG(`price`), 2) AS avg_price FROM `spacenk_listing` WHERE `price`<>'' GROUP BY `brand` ORDER BY avg_price DESC";
$result = $conn->query($sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $brand = $row["brand"];
    $avg_price = $row["avg_price"];

    $brand = real_value($brand);
    $html = "<tr>
              <td>$colum</td>
              <td>$brand</td>
              <td>$avg_price</td>
            </tr>";
    echo $html;

  }
}


$conn->close();
?>

  </table>
</div>

</body>
</html> 