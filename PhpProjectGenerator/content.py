footer = "<script src='Assets/js/index.js'></script>"

header = """

<!DOCTYPE html>
<html lang="en">
<head>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- jQuery CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    
    <!-- CUSTOM CSS -->
    <link rel="stylesheet" href="Assets/css/index.css">

    <!-- Font Awesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<!-- Boostrap 4 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
	
    <meta charset="UTF-8">
	<title>Your title</title>
</head>

"""

index = """ 
<?php

$p = "";

if(isset($_GET['p'])) {
	$p = $_GET['p'];
} else {
	$p = "Main file here";
}

?>

<?php include("Core/Components/Header.php"); ?>

<body>

	<section id='p'>
		<?php include("Core/View/" .  $p . ".php"); ?>
	</section>
	
</body>

<?php include("Core/Components/Footer.php"); ?>

</html>
"""

css = "*{margin:0px; padding:0px; box-sizing:border-box;}"

js = "$(document).ready(ready);"