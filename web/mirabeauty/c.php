<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>Reviews source report sorted by review count</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>No</th>
        <th>Source</th>
        <th>Count</th>
        <th>%</th>
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

$total_reviews_sql = "SELECT SUM(`review`) AS total_reviews FROM `listing`";
$total_reviews_result = $conn->query($total_reviews_sql);
$total_reviews = 0;
$colum = 0;
if ($total_reviews_result->num_rows > 0) {
  // output data of each row
  while($total_reviews_row = $total_reviews_result->fetch_assoc()) {
    $total_reviews = $total_reviews_row["total_reviews"];
  }
}
function in_array_case_insensitive($needle, $haystack) 
{
 return in_array( strtolower($needle), array_map('strtolower', $haystack) );
}

$array_review_websites = array();
$sql = "SELECT DISTINCT `review_websites` FROM `listing` WHERE `review_websites`<>''";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    $review_websites_temp = $row['review_websites'];
    $str_arr = explode (",", $row['review_websites']); 
    foreach ($str_arr as $str) {
      if (!in_array_case_insensitive(trim($str), $array_review_websites)) {
        array_push($array_review_websites, trim($str));
      }
    }
    
  }
}
sort($array_review_websites);
// var_dump($array_review_websites);

$colum = 0;
foreach ($array_review_websites as $value) {
  $colum ++;
  $get_count_sql = "SELECT SUM(`review`) AS total_review FROM `listing` WHERE `review_websites` LIKE '%$value%'";
    $count_result = $conn->query($get_count_sql);
    $total_review = 0;
    if ($count_result->num_rows > 0) {
      // output data of each row
      while($count_row = $count_result->fetch_assoc()) {
        $total_review = $count_row["total_review"];
      }
    }
    $review_percent = $total_review / $total_reviews * 100;
    $review_percent = round($review_percent, 2);
    $source = real_value($value);
    $html = "<tr>
              <td>$colum</td>
              <td>$source</td>
              <td>$total_review</td>
              <td>$review_percent</td>
            </tr>";
    echo $html;
}
// $sql = "select id, substring_index( substring_index(`review_websites`, ',', n), ',', -1 ) as `review_website` from listing join numbers on char_length(`review_websites`) - char_length(replace(`review_websites`, ',', '')) >= n - 1 WHERE `review_websites`<>'' GROUP BY `review_website`";
// $result = $conn->query($sql);
// $colum = 0;
// if ($result->num_rows > 0) {
//   // output data of each row
//   while($row = $result->fetch_assoc()) {
//     $colum ++;
//     $review_website = $row["review_website"];
//     

//   }
// }


$conn->close();
?>

  </table>
</div>

</body>
</html> 