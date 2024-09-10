<?php
$to = "mh8936000@gmail.com";
$subject = "Test mail";
$message = "Hello! This is a test email message.";
$from = "drggames@yahoo.com";
$headers = "From:" . $from;

mail($to,$subject,$message,$headers)
?>