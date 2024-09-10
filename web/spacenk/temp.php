<?php

$category_array = array("Treatment", "Skincare", "Complexion", "Moisturisers", "Cleansers", "Makeup", "Personal Fragrance", " Hair Treatment", "Eyes", "Styling", "Fragrance", "Haircare", "Cheeks", "Lipcare", "Bath & Body", "Shampoo", "Eyecare", "Toner", "Lips", "Electronic", "Conditioner", "Body Cleanser ", "Tools", "Body Moisturiser & Oils", "Accessories", "Suncare", "Home Fragrance", "Makeup Brushes", "Sun & Tan", "Tanning", "Aromatherapy", "Stocking Fillers", "Skincare Set", "Sets & Palettes", "Deodorant", "Body Treatment", "Neck & Decollete", "Bath & Body Set", "Haircare Sets", "After Suncare", "Books", "Bag", "Wellness", "Nails", "Oral Hygiene", "Mens Grooming", "Brands", "A", "Christmas", "Glow Makeup", "S", "Gifts Under £50", "R");

function f($level, $array){
  // var_dump($array);
  if($level==1){
    echo "<br>";
    return;
  }
  $arr=$array;
  for($i=0; $i<52-$level; $i++){
    echo $arr[$i] .", ";
    unset($arr[$i]);
    $arr = array_values($arr);
    f($level-1, $arr);
  }

}
$category_array_count = count($category_array);
f(2, $category_array);

?>