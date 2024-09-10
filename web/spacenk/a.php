<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Brand report sorted by total number of products</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Brand</th>
        <th>Total projects</th>
        <th>Product marketshare %</th>
        <th>Total reviews</th>
        <th>Review marketshare %</th>
        <th>Avg rating</th>
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

$sql = "SELECT `brand`, COUNT(`product`) AS total_product, SUM(`reviews`) AS total_reviews, Round(AVG(`rating`), 2) AS avg_rating FROM `spacenk_listing` GROUP BY `brand` ORDER BY total_product DESC";
$result = $conn->query($sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $brand = $row["brand"];
    $total_product = 0;
    $total_reviews = 0;
    $avg_rating = 0;
    $total_product = $row["total_product"];
    $total_reviews = $row["total_reviews"];
    $avg_rating = $row["avg_rating"];


    $product_mar_percent = round($total_product / 2934 * 100, 2);
    $review_mar_percent = round($total_reviews / 164565 * 100, 2);

    $brand = real_value($brand);
    $html = "<tr>
              <td>$colum</td>
              <td>$brand</td>
              <td>$total_product</td>
              <td>$product_mar_percent</td>
              <td>$total_reviews</td>
              <td>$review_mar_percent</td>
              <td>$avg_rating</td>
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