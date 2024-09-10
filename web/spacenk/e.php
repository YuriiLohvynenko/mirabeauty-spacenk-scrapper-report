<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Top product categories sorted by most reviews</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Category</th>
        <th>Products</th>
        <th>Brand</th>
        <th>Reviews</th>
        <th>Average price</th>
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

$sql = "SELECT `real_category`, Round(AVG(`price`), 2) AS avg_price, SUM(`reviews`) AS total_reviews, COUNT(`product`) AS total_product, COUNT(DISTINCT `brand`) AS total_brand FROM `spacenk_listing` WHERE `price`<>'' GROUP BY `real_category` ORDER BY total_reviews DESC";
$result = $conn->query($sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $category = $row["real_category"];
    $avg_price = $row["avg_price"];
    $total_reviews = $row["total_reviews"];
    $total_product = $row["total_product"];
    $total_brand = $row["total_brand"];

    $category = real_value($category);
    

    $html = "<tr>
              <td>$colum</td>
              <td>$category</td>
              <td>$total_product</td>
              <td>$total_brand</td>
              <td>$total_reviews</td>
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