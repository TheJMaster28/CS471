all: ada cshell perl php
ada:
	gcc -c pro2ada.adb
	gnatmake --GNATBIND=gnatbind --GNATLINK=gnatlink pro2ada
	$(info ---------Ada---------)
	./pro2ada
cshell:
	$(info ---------C-Shell---------)
	./pro2CShell
perl:
	$(info ---------PERL---------)
	perl pro2Perl.pl
php:
	$(info ---------PHP---------)
	php -d display_errors=on pro2PHP.php