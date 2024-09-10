<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Top 1000 products report sorted by review count</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Product</th>
        <th>Brand</th>
        <th>Review count</th>
        <th>Checkout</th>
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

$brand_get_sql = "SELECT `product`, `brand`, `review`, `checkout` FROM `listing` ORDER BY `review` DESC LIMIT 1000";
$result = $conn->query($brand_get_sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $brand = real_value($row["brand"]);
    $product = real_value($row["product"]);
    $review = real_value($row["review"]);
    $checkout = real_value($row["checkout"]);
    if ($checkout == 'Add to Cart') {
      $checkout = 'Fullfillment';
    }
    $html = "<tr>
              <td>$colum</td>
              <td>$product</td>
              <td>$brand</td>
              <td>$review</td>
              <td>$checkout</td>
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