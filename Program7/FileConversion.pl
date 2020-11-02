#!/usr/bin/perl
# Jeffrey Lansford
# 11/2/2020
# Program 7
# Perl version of removing content from file when seeing a Control-C and stopping when seeing a Control-B

use strict;
use warnings;

# file name arguments for in and out
my ($fileInputName,$fileOutputName) = @ARGV;

# open  Input file 
open(INPUT, "<".$fileInputName) or die "Couldnt open file, $!";

# open Output file
open(OUTPUT, ">".$fileOutputName) or die "Couldnt open file, $!";

# set to writing mode
my $deleteMode = 0;
while(1) {
    # read a charcter at a time  
    my $char;
    read INPUT, $char, 1;

    # reached end of file
    if (!ord($char)) {
        last;
    }

    # start delete mode when seeing a Control-C character ascii value
    if (ord($char) == 3) {
        $deleteMode = 1;
    } 

    # write to oupt when in write mode
    if (!$deleteMode) {
        print OUTPUT $char;
    }

    # switch to write mode when seeing a Control-B character ascii value
    if (ord($char) == 2) {
        $deleteMode = 0;
    }

}

# close files
close(INPUT) || die "Couldn't close file properly";
close(OUTPUT) || die "Couldn't close file properly";

print "Successfully wrote to control-char-output-Perl.txt\n";

