<?php
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

$sql = "SELECT * FROM `listing2` ORDER BY id ASC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
  	$brand = $row["brand"];
  	$category = $row["category"];
  	$product = $row["product"];
  	$price = $row["price"];
  	$rating = $row["rating"];
  	$review = $row["review"];
  	$viewon_first = $row["viewon_first"];
  	$viewon_link = $row["viewon_link"];
  	$checkout = $row["checkout"];
  	$fullfilledby = $row["fullfilledby"];

  	$alternative_retailers_first = $row["alternative_retailers_first"];
  	$alternative_retailers_link = $row["alternative_retailers_link"];
  	$review_websites = $row["review_websites"];
  	$button_statue = $row["button_statue"];
  	$product_url = $row["product_url"];
  	
  		// $insert_sql = "INSERT INTO `listing`(`brand`, `category`, `product`, `price`, `rating`, `review`, `viewon_first`, `viewon_link`, `checkout`, `fullfilledby`, `alternative_retailers_first`, `alternative_retailers_link`, `review_websites`, `button_statue`, `product_url`) VALUES ('$brand','$category','$product','$price','$rating',$review,'$viewon_first','$viewon_link','$checkout','$fullfilledby','$alternative_retailers_first','$alternative_retailers_link','$review_websites','$button_statue','$product_url')";
  		// $conn->query($insert_sql);
  	
  	

  }
} else {
  echo "0 results";
}
$conn->close();
?>