#!/usr/bin/perl
# Jeffrey Lansford
# 9/9/2020
# Program 2
# Perl program to test the short circut implementation of Perl
use strict;
use warnings;

print "A is always False and B is always True\n";

# Function to show evaluation of B in evaluations
sub b {
    print "\twithin b\n";
    return 1;  
}

# Set A to value to compare with to equte 'False'
$a = 1;


# Short Circut evaluation on 'and' in Perl
# evaluate A to false and run B() and return 1 to evaluate to true
print "A && B\n";
if ($a == 0 && b()) {
    print "True\n";
}
else{
    print "False\n";
}

# run B() and return 1 to evaluate to true and evaluate A to false
print "B && A\n";
if ( b() && $a == 0) {
    print "True\n";
}
else{
    print "False\n";
}



