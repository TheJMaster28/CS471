<?php
// Jeffrey Lansford
// 9/9/2020
// Program 2
// PHP program to test the short circut implementation of PHP
echo "A is always False and B is always True\n";

// B function for testing if it is evaluated within and statement
function b () {
    echo "\twithin b\n";
    return true;
}
$a = false;

# Short Circut evalution on 'and' in PHP
# evaluate A to false and run B() and evaluate to true
echo "A && B\n";
if ($a && b()) {
    echo "True\n";
}
else {
    echo "False\n";
}

# run B() and evaluate to true and evaluate A to false
echo "B && A\n";
if (b() && $a ) {
    echo "True\n";
}
else {
    echo "False\n";
}


?>