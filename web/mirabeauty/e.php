<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Report per Category</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Category</th>
        <th>Number of products per Category</th>
        <th>Number of brands per Category</th>
        <th>Total reviews per Category</th>
        <th>Average product Price</th>
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

$category_get_sql = "SELECT DISTINCT `category` FROM `listing` ORDER BY `category` ASC";
$result = $conn->query($category_get_sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $category = $row["category"];
    $product_count = 0;
    $brand_count = 0;
    $total_reviews = 0;
    $count_get_sql = "SELECT COUNT(`product`) AS product_count, COUNT(DISTINCT `brand`) AS brand_count, SUM(review) AS total_reviews FROM `listing` WHERE `category`='$category'";
    $count_result = $conn->query($count_get_sql);
    if ($count_result->num_rows > 0) {
      // output data of each row
      while($count_row = $count_result->fetch_assoc()) {
        $product_count =  $count_row["product_count"];
        $brand_count = $count_row["brand_count"];
        $total_reviews = $count_row["total_reviews"];
      }
    }

    $avgprice_get_sql = "SELECT AVG(`real_price`) AS avgprice FROM `listing` WHERE `category`='$category' AND `real_price`<>''";
    $avgprice_result = $conn->query($avgprice_get_sql);
    $avgprice = 0;
    if ($avgprice_result->num_rows > 0) {
      // output data of each row
      while($avgprice_row = $avgprice_result->fetch_assoc()) {
        $avgprice = round($avgprice_row["avgprice"],2);
      }
    }
      
    $html = "<tr>
              <td>$colum</td>
              <td>$category</td>
              <td>$product_count</td>
              <td>$brand_count</td>
              <td>$total_reviews</td>
              <td>$avgprice</td>
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