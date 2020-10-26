// Jeffrey Lansford
// Chapter 9 problem
// 10/20/2020
// run with Node.js with the folling command `node chapter9.js`

function sub1() {
   var x;
   function sub2() {
      // alert(x);
      console.log(x);
   }
   function sub3() {
      var x;
      x = 3;
      sub4(sub2);
   }
   function sub4(subx) {
      var x;
      x = 4;
      subx();
   }
   x = 1;
   sub3();
}

sub1();
