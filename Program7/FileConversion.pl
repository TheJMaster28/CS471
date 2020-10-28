#!/usr/bin/perl

use strict;
use warnings;

print "Perl\n";
open(INPUT, "<control-char.txt") or die "Couldnt open file, $!";
open(OUTPUT, ">control-char-output-Perl.txt") or die "Couldnt open file, $!";
my $deleteMode = 0;
while(1) {
    my $char;
    read INPUT, $char, 1;

    if (!ord($char)) {
        last;
    }

    if (ord($char) == 3) {
        $deleteMode = 1;
    } 

    if (!$deleteMode) {
        print OUTPUT $char;
    }

    if (ord($char) == 2) {
        $deleteMode = 0;
    }

}



close(INPUT) || die "Couldn't close file properly";
close(OUTPUT) || die "Couldn't close file properly";
