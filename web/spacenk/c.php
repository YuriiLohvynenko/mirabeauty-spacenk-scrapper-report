<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Top 1000 products sorted by review count</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Product</th>
        <th>Price</th>
        <th>Brand</th>
        <th>Review count</th>
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

$sql = "SELECT `product`, `price`, `brand`, `reviews` FROM `spacenk_listing` ORDER BY `reviews` DESC LIMIT 1000";
$result = $conn->query($sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $product = $row["product"];
    $price = $row["price"];
    $brand = $row["brand"];
    $reviews = $row["reviews"];

    $product = real_value($product);
    $brand = real_value($brand);

    $html = "<tr>
              <td>$colum</td>
              <td>$product</td>
              <td>$price</td>
              <td>$brand</td>
              <td>$reviews</td>
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