<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">
  <h2>User statistics</h2>

  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr >
        <th></th>
        <th>QTY</th>
        <th></th>
        <th></th>
      </tr>
    </thead>
    <tr>
      <td>Total User</td>
      <td>26648</td>
      <td></td>
      <td></td>
    <tr>
    <tr>
      <td>Average reviews per user</td>
      <td>6.25</td>
      <td></td>
      <td></td>
    <tr>
    <tr>
      <td>Average reviews last 12 months</td>
      <td>4.32</td>
      <td></td>
      <td></td>
    <tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    <tr>    
    <tr>
      <th>Gender</th>
      <th>QTY</th>
      <th> % </th>
      <th>Price</th>
    <tr> 
    <tr>
      <td>Female</td>
      <td>7959</td>
      <td>29.86</td>
      <td></td>
    </tr>
    <tr>
      <td>Male</td>
      <td>626</td>
      <td>2.34</td>
      <td></td>
    </tr>
    <tr>
      <td>etc</td>
      <td>18063</td>
      <td>67.8</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    <tr>    
    <tr>
      <th>Age range</th>
      <th>QTY</th>
      <th> % </th>
      <th>Price</th>
    <tr> 
    <tr>
      <td>Under 30</td>
      <td>108</td>
      <td>0.405</td>
      <td></td>
    <tr>
    <tr>
      <td>30-45</td>
      <td>172</td>
      <td>0.645</td>
      <td></td>
    <tr> 
    <tr>
      <td>45+</td>
      <td>58</td>
      <td>0.217</td>
      <td></td>
    <tr> 
    <tr>
      <td>etc</td>
      <td>26310</td>
      <td>98.73</td>
      <td></td>
    <tr>  
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    <tr>    
    <tr>
      <th>Top 50 locations</th>
      <th></th>
      <th></th>
      <th></th>
    <tr>  
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

$review_last_sql = "SELECT COUNT(`id`) AS last_total_reviews, COUNT(DISTINCT `username`) AS last_users FROM `spacenk_review` WHERE `review_date` LIKE '%days ago%' OR `review_date` LIKE '%months ago%' OR `review_date` LIKE '%hours ago%' OR `review_date` LIKE '%minutes ago%'";
$last_reviews = 0;
$last_reviews_result = $conn->query($review_last_sql);
if ($last_reviews_result->num_rows > 0) {
  // output data of each row
  while($last_reviews_row = $last_reviews_result->fetch_assoc()) {
    $last_reviews = round($last_reviews_row["last_total_reviews"] / $last_reviews_row["last_users"], 2);
  }
}

$female_get_sql = "SELECT `gender`, COUNT(`id`) FROM `spacenk_user` GROUP BY `gender`";
$age_get_sql = "SELECT `age`, COUNT(`id`) FROM `spacenk_user` GROUP BY `age`";
$location_get_sql = "SELECT `location`, COUNT(DISTINCT `username`) AS total_reviews FROM `spacenk_review` where location<>'' GROUP BY `location` ORDER BY total_reviews DESC LIMIT 52";
// $location_get_sql = "SELECT `username`, `location`, COUNT(`id`) AS total_counts FROM `spacenk_review` GROUP BY `username` ORDER BY total_counts DESC LIMIT 50";
$location_get_result = $conn->query($location_get_sql);
if ($location_get_result->num_rows > 0) {
  // output data of each row
  while($location_get_row = $location_get_result->fetch_assoc())
  {
    $total_reviews = $location_get_row["total_reviews"];
    $location = $location_get_row["location"];;
    $html = "
          <tr>
            <td>$location</td>
            <td>$total_reviews</td>
            <td></td>
            <td></td>
          <tr>  
        ";
    echo $html;
    
    

  }
}

$category_get_sql = "SELECT `real_category`, COUNT(`id`) AS total_count FROM `spacenk_review` GROUP BY `real_category` ORDER BY total_count DESC";
$category_results = $conn->query($category_get_sql);
$a = array();
$b = array();
if ($category_results->num_rows > 0) {
  while($category_row = $category_results->fetch_assoc())
  {
    array_push($a, $category_row["real_category"]);
    array_push($b, $category_row["real_category"]);
  }
}
echo "
  <tr>
    <th>Top category combination</th>
    <th></th>
    <th></th>
    <th></th>
  <tr> 
";
foreach ($a as $a_value) {
  foreach ($b as $b_value) {
    if ($a_value != $b_value) {
      $content_show_sql = "SELECT COUNT(`id`) AS total_count1 FROM `spacenk_review` WHERE `real_category`='$a_value' AND `real_category`='$b_value'";
      $content_show_results = $conn->query($content_show_sql);
      if ($content_show_results->num_rows > 0) {
        while ($content_show_row = $content_show_results->fetch_assoc()) {
          $total_count1 = $content_show_row["total_count1"];
          if ($total_count1 != 0) {
            $html = "
              <tr>
                <td>$a_value, $b_value</td>
                <td>$total_count1</td>
                <td></td>
                <td></td>
              <tr>
            ";
          echo $html;
          }
          
        }
      }
    }
  }
}

$temp_sql = "SELECT `username`, `real_category`, COUNT(`id`) FROM `spacenk_review` GROUP BY `username`, `real_category`";
$two_combine_sql = "SELECT `Treatment`, `Skincare` FROM `category_combination` WHERE `Treatment`<>'' AND `Skincare`<>''";
$two_combine_results = $conn->query($two_combine_sql);
$combine_show_value = 0;
if ($two_combine_results->num_rows>0) {
  while ($two_combine_row = $two_combine_results->fetch_assoc()) {
    $combine_value =  min($two_combine_row['Treatment'], $two_combine_row['Skincare']);
    $combine_show_value = $combine_show_value + $combine_value;
  }
}
echo "
  <tr>
    <td>Treatment, Skincare</td>
    <td>$combine_show_value</td>
    <td></td>
    <td></td>
  <tr> 
";
$three_combine_sql = "SELECT `Treatment`, `Skincare`,`Complexion` FROM `category_combination` WHERE `Treatment`<>'' AND `Skincare`<>'' AND `Complexion`<>''";
$three_combine_results = $conn->query($three_combine_sql);
$combine_show_value = 0;
if ($three_combine_results->num_rows>0) {
  while ($three_combine_row = $three_combine_results->fetch_assoc()) {
    $combine_value =  min($three_combine_row['Treatment'], $three_combine_row['Skincare'], $three_combine_row['Complexion']);
    // echo $combine_value."<br>";
    $combine_show_value = $combine_show_value + $combine_value;
  }
}
echo "
  <tr>
    <td>Treatment, Skincare, Complexion</td>
    <td>$combine_show_value</td>
    <td></td>
    <td></td>
  <tr> 
";
$four_combine_sql = "SELECT `Treatment`, `Skincare`,`Complexion`, `Moisturisers` FROM `category_combination` WHERE `Treatment`<>'' AND `Skincare`<>'' AND `Complexion`<>'' AND `Moisturisers`<>''";
$four_combine_results = $conn->query($four_combine_sql);
$combine_show_value = 0;
if ($four_combine_results->num_rows>0) {
  while ($four_combine_row = $four_combine_results->fetch_assoc()) {
    $combine_value =  min($four_combine_row['Treatment'], $four_combine_row['Skincare'], $four_combine_row['Complexion'], $four_combine_row['Moisturisers']);
    // echo $combine_value."<br>";
    $combine_show_value = $combine_show_value + $combine_value;
  }
}
echo "
  <tr>
    <td>Treatment, Skincare, Complexion, Moisturisers</td>
    <td>$combine_show_value</td>
    <td></td>
    <td></td>
  <tr> 
";
$five_combine_sql = "SELECT `Treatment`, `Skincare`,`Complexion`, `Moisturisers`, `Cleansers` FROM `category_combination` WHERE `Treatment`<>'' AND `Skincare`<>'' AND `Complexion`<>'' AND `Moisturisers`<>'' AND `Cleansers`<>''";
$five_combine_results = $conn->query($five_combine_sql);
$combine_show_value = 0;
if ($five_combine_results->num_rows>0) {
  while ($five_combine_row = $five_combine_results->fetch_assoc()) {
    $combine_value =  min($five_combine_row['Treatment'], $five_combine_row['Skincare'], $five_combine_row['Complexion'], $five_combine_row['Moisturisers'], $five_combine_row['Cleansers']);
    // echo $combine_value."<br>";
    $combine_show_value = $combine_show_value + $combine_value;
  }
}
echo "
  <tr>
    <td>Treatment, Skincare, Complexion, Moisturisers, Cleansers</td>
    <td>$combine_show_value</td>
    <td></td>
    <td></td>
  <tr> 
";
$six_combine_sql = "SELECT `Treatment`, `Skincare`,`Complexion`, `Moisturisers`, `Cleansers`, `Makeup` FROM `category_combination` WHERE `Treatment`<>'' AND `Skincare`<>'' AND `Complexion`<>'' AND `Moisturisers`<>'' AND `Cleansers`<>'' AND `Makeup`<>''";
$six_combine_results = $conn->query($six_combine_sql);
$combine_show_value = 0;
if ($six_combine_results->num_rows>0) {
  while ($six_combine_row = $six_combine_results->fetch_assoc()) {
    $combine_value =  min($six_combine_row['Treatment'], $six_combine_row['Skincare'], $six_combine_row['Complexion'], $six_combine_row['Moisturisers'], $six_combine_row['Cleansers'], $six_combine_row['Makeup']);
    // echo $combine_value."<br>";
    $combine_show_value = $combine_show_value + $combine_value;
  }
}
echo "
  <tr>
    <td>Treatment, Skincare, Complexion, Moisturisers, Cleansers, Makeup</td>
    <td>$combine_show_value</td>
    <td></td>
    <td></td>
  <tr> 
";
// $seven_combine_sql = "SELECT `Treatment`, `Skincare`,`Complexion`, `Moisturisers`, `Cleansers`, `Makeup` FROM `category_combination` WHERE `Treatment`<>'' AND `Skincare`<>'' AND `Complexion`<>'' AND `Moisturisers`<>'' AND `Cleansers`<>'' AND `Makeup`<>''";
// $seven_combine_results = $conn->query($seven_combine_sql);
// $combine_show_value = 0;
// if ($seven_combine_results->num_rows>0) {
//   while ($seven_combine_row = $seven_combine_results->fetch_assoc()) {
//     $combine_value =  min($seven_combine_row['Treatment'], $seven_combine_row['Skincare'], $seven_combine_row['Complexion'], $seven_combine_row['Moisturisers'], $seven_combine_row['Cleansers'], $seven_combine_row['Makeup']);
//     // echo $combine_value."<br>";
//     $combine_show_value = $combine_show_value + $combine_value;
//   }
// }
// echo "
//   <tr>
//     <td>Treatment, Skincare, Complexion, Moisturisers, Cleansers, Makeup</td>
//     <td>$combine_show_value</td>
//     <td></td>
//     <td></td>
//   <tr> 
// ";
$category_array = array("Treatment", "Skincare", "Complexion", "Moisturisers", "Cleansers", "Makeup", "Personal Fragrance", " Hair Treatment", "Eyes", "Styling", "Fragrance", "Haircare", "Cheeks", "Lipcare", "Bath & Body", "Shampoo", "Eyecare", "Toner", "Lips", "Electronic", "Conditioner", "Body Cleanser ", "Tools", "Body Moisturiser & Oils", "Accessories", "Suncare", "Home Fragrance", "Makeup Brushes", "Sun & Tan", "Tanning", "Aromatherapy", "Stocking Fillers", "Skincare Set", "Sets & Palettes", "Deodorant", "Body Treatment", "Neck & Decollete", "Bath & Body Set", "Haircare Sets", "After Suncare", "Books", "Bag", "Wellness", "Nails", "Oral Hygiene", "Mens Grooming", "Brands", "A", "Christmas", "Glow Makeup", "S", "Gifts Under £50", "R");

// function f($level, $array){
//   // var_dump($array);
//   if($level==1){
//     echo "<br>";
//     return;
//   }
//   $arr=$array;
//   for($i=0; $i<52-$level; $i++){
//     echo $arr[$i] .", ";
//     unset($arr[$i]);
//     $arr = array_values($arr);
//     f($level-1, $arr);
//   }

// }
// $category_array_count = count($category_array);
// f(2, $category_array);

// var_dump($category_array);
// $sql = "SELECT `real_category`, Round(AVG(`price`), 2) AS avg_price, SUM(`reviews`) AS total_reviews, COUNT(`product`) AS total_product, COUNT(DISTINCT `brand`) AS total_brand FROM `spacenk_listing` WHERE `price`<>'' GROUP BY `category` ORDER BY total_reviews DESC";
// $result = $conn->query($sql);
// $colum = 0;
// if ($result->num_rows > 0) {
//   // output data of each row
//   while($row = $result->fetch_assoc()) {
//     $colum ++;
//     $category = $row["real_category"];
//     $avg_price = $row["avg_price"];
//     $total_reviews = $row["total_reviews"];
//     $total_product = $row["total_product"];
//     $total_brand = $row["total_brand"];

//     $category = real_value($category);
    

//     $html = "<tr>
//               <td>$colum</td>
//               <td>$category</td>
//               <td>$total_product</td>
//               <td>$total_brand</td>
//               <td>$total_reviews</td>
//               <td>$avg_price</td>
//             </tr>";
//     echo $html;

//   }
// }


$conn->close();
?>

  </table>
</div>

</body>
</html> 