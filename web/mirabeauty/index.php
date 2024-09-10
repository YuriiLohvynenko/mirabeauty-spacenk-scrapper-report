<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Brand report sorted by total products</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Brand</th>
        <th>Total projects</th>
        <th>Average price</th>
        <th>Retailers</th>
        <th>Product marketshare %</th>
        <th>Product fullfillment %</th>
        <th>Product link %</th>
        <th>Product alt link %</th>
        <th>Total reviews</th>
        <th>Rating</th>
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

$brand_get_sql = "SELECT DISTINCT `brand` FROM `listing`";
$result = $conn->query($brand_get_sql);
$colum = 0;
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    $colum ++;
    $brand = $row["brand"];
    $total_product = 0;
    $total_reviews = 0;
    $avg_rating = 0;
    $total_product_sql = "SELECT COUNT(product) AS total_product, SUM(`review`) AS total_reviews, ROUND(AVG(`rating`),2) AS avg_rating FROM `listing` WHERE `brand`='$brand'";
    $total_product_result = $conn->query($total_product_sql);
    if ($total_product_result->num_rows > 0) {
      // output data of each row
      while($total_product_row = $total_product_result->fetch_assoc()) {
        $total_product = $total_product_row["total_product"];
        $total_reviews = $total_product_row["total_reviews"];
        $avg_rating = $total_product_row["avg_rating"];
      }
    }
    $fullfilledby_count = 0;
    $fullfilledby_sql = "SELECT COUNT(fullfilledby) AS fullfilledby_count FROM `listing` WHERE `brand`='$brand' AND `fullfilledby`<>''";
    $fullfilledby_result = $conn->query($fullfilledby_sql);
    if ($fullfilledby_result->num_rows > 0) {
      // output data of each row
      while($fullfilledby_row = $fullfilledby_result->fetch_assoc()) {
        $fullfilledby_count = $fullfilledby_row["fullfilledby_count"];
      }
    }

    $product_link_count = 0;
    $product_link_sql = "SELECT COUNT(`viewon_first`) AS product_link_count FROM `listing` WHERE `brand`='$brand' AND `viewon_first`<>''";
    $product_link_result = $conn->query($product_link_sql);
    if ($product_link_result->num_rows > 0) {
      // output data of each row
      while($product_link_row = $product_link_result->fetch_assoc()) {
        $product_link_count = $product_link_row["product_link_count"];
      }
    }

    $product_alt_link_count = 0;
    $product_alt_link_sql = "SELECT COUNT(`alternative_retailers_first`) AS product_alt_link_count FROM `listing` WHERE `brand`='$brand' AND `alternative_retailers_first`<>''";
    $product_alt_link_result = $conn->query($product_alt_link_sql);
    if ($product_alt_link_result->num_rows > 0) {
      // output data of each row
      while($product_alt_link_row = $product_alt_link_result->fetch_assoc()) {
        $product_alt_link_count = $product_alt_link_row["product_alt_link_count"];
      }
    }
    $brand = real_value($brand);
    $fullfilledby_percent = round($fullfilledby_count / $total_product * 100, 2);
    $product_link_percent = round($product_link_count / $total_product * 100, 2);
    $product_alt_link_percent = round($product_alt_link_count / $total_product * 100, 2);
    $product_mar_percent = round($total_product / 51887 * 100, 2);

    $avgprice_sql = "SELECT AVG(`real_price`) AS avgprice FROM `listing` WHERE `brand`='$brand' AND `real_price`<>''";
    $avgprice_result = $conn->query($avgprice_sql);
    $avgprice = 0;
    if ($avgprice_result->num_rows > 0) {
      // output data of each row
      while($avgprice_row = $avgprice_result->fetch_assoc()) {
        $avgprice = round($avgprice_row["avgprice"], 2);
      }
    }

    // $retailer_get_sql = "";
    // $retailer_result = $conn->query($retailer_get_sql);
    $retailer_count = $fullfilledby_count + $product_link_count + $product_alt_link_count;
    

    $html = "<tr>
              <td>$colum</td>
              <td>$brand</td>
              <td>$total_product</td>
              <td>$avgprice</td>
              <td>$retailer_count</td>
              <td>$product_mar_percent</td>
              <td>$fullfilledby_percent</td>
              <td>$product_link_percent</td>
              <td>$product_alt_link_percent</td>
              <td>$total_reviews</td>
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