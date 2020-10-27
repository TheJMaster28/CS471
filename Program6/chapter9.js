// Jeffrey Lansford
// Chapter 9 problem
// 10/20/2020
// program to test JavaScript binding of global varibles during subroutine passing
// run with Node.js with the following command `node chapter9.js`

function sub1() {
   var x;
   function sub2() {
      // alert(x);
      console.log(`x = ${x}`);
      if (x == 1) {
         console.log("JavaScript is Deep Binding");
      } else if (x == 4) {
         console.log("JavaScript is Shallow Binding");
      } else if (x == 3) {
         console.log("JavaScript is Ad Hoc Binding");
      } else {
         console.log("Something is wrong...");
      }
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
