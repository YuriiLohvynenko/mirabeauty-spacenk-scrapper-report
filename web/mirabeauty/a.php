<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Retailer report sorted by total brands</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Retailer</th>
        <th>Total brands</th>
        <th>Brand marketshare %</th>
        <th>Total projects</th>
        <th>Product marketshare %</th>
        <th>Product fullfillment %</th>
        <th>Product link %</th>
        <th>Product alt link %</th>
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

$retailer_get_sql = "SELECT DISTINCT `viewon_first` FROM `listing` WHERE `viewon_first`<>''";
$result = $conn->query($retailer_get_sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $retailer = $row["viewon_first"];
    $total_brand = 0;

    $total_product = 0;

    $total_product_sql = "SELECT COUNT(DISTINCT `brand`) AS total_brand, COUNT(DISTINCT `product`) AS total_product FROM `listing` WHERE `viewon_first`='$retailer' OR `fullfilledby`='$retailer' OR `alternative_retailers_first`='$retailer'";
    $total_product_result = $conn->query($total_product_sql);
    if ($total_product_result->num_rows > 0) {
      // output data of each row
      while($total_product_row = $total_product_result->fetch_assoc()) {
        $total_product = $total_product_row["total_product"];
        $total_brand = $total_product_row["total_brand"];
      }
    }
    $fullfilledby_count = 0;
    $fullfilledby_sql = "SELECT COUNT(product) AS fullfilledby_count FROM `listing` WHERE `fullfilledby`='$retailer'";
    $fullfilledby_result = $conn->query($fullfilledby_sql);
    if ($fullfilledby_result->num_rows > 0) {
      // output data of each row
      while($fullfilledby_row = $fullfilledby_result->fetch_assoc()) {
        $fullfilledby_count = $fullfilledby_row["fullfilledby_count"];
      }
    }

    $product_link_count = 0;
    $product_link_sql = "SELECT COUNT(product) AS product_link_count FROM `listing` WHERE `viewon_first`='$retailer'";
    $product_link_result = $conn->query($product_link_sql);
    if ($product_link_result->num_rows > 0) {
      // output data of each row
      while($product_link_row = $product_link_result->fetch_assoc()) {
        $product_link_count = $product_link_row["product_link_count"];
      }
    }

    $product_alt_link_count = 0;
    $product_alt_link_sql = "SELECT COUNT(product) AS product_alt_link_count FROM `listing` WHERE `alternative_retailers_first`='$retailer'";
    $product_alt_link_result = $conn->query($product_alt_link_sql);
    if ($product_alt_link_result->num_rows > 0) {
      // output data of each row
      while($product_alt_link_row = $product_alt_link_result->fetch_assoc()) {
        $product_alt_link_count = $product_alt_link_row["product_alt_link_count"];
      }
    }
    $retailer = real_value($retailer);
    $fullfilledby_percent = round($fullfilledby_count / $total_product * 100, 2);
    $product_link_percent = round($product_link_count / $total_product * 100, 2);
    $product_alt_link_percent = round($product_alt_link_count / $total_product * 100, 2);
    $product_mar_percent = round($total_product / 51887 * 100, 2);
    $brand_mar_percent = round($total_brand / 641 * 100, 2);
    $html = "<tr>
              <td>$colum</td>
              <td>$retailer</td>
              <td>$total_brand</td>
              <td>$brand_mar_percent</td>
              <td>$total_product</td>
              <td>$product_mar_percent</td>
              <td>$fullfilledby_percent</td>
              <td>$product_link_percent</td>
              <td>$product_alt_link_percent</td>
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