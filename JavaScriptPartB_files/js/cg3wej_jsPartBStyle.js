/*
  
  SAVE AND RENAME THE JS FILE (AND REFERENCES - 
  LINK TAG) TO MATCH THE ASSIGNMENT REQUIREMENTS:
		cg3xzz_jsPartBStyle.js 
  
  IN THIS FILE YOU SHOULD DEFINE THREE FUNCTIONS:
  incr(), decr(), and redir(). THEY WILL BE HOOKED
  UP TO THE THREE CORRESPONDING BUTTONS IN YOUR
  HTML FILE.

  incr() WILL TAKE THE CURRENT NUMBER IN YOUR counter
  ELEMENT AND INCREASE IT BY ONE. THERE IS NO LIMIT TO
  HOW HIGH incr() CAN INCREASE THE NUMBER.

  decr() WILL DO THE SAME AS incr() EXCEPT IT WILL
  DECREASE THE NUMBER. ALSO, YOU SHOULD UTILIZE
  CONTROL FOLOW IN decr() TO ONLY ALLOW THE USER TO
  DECREASE THE NUMBER TO 0. IF THEY TRY TO DECREASE
  LOWER THAN 0, SHOW AN ALERT WARNING THE USER THAT
  THEY CANNOT DO SO. YOU CAN WRITE WHATEVER YOU'D LIKE
  IN THE ERROR MESSAGE.

  redir() WILL REDIRECT THE USER TO YOUR CODECADEMY PROFILE.
  ENSURE THAT YOUR PROFILE IS PUBLIC AND THAT YOU HAVE COMPLETED
  THE FIRST 8 JAVASCRIPT LESSONS AS WE WILL BE CHECKING THE BADGES.
  YOU SHOULD DO THE REDIRECT COMPLETELY THROUGH JAVASCRIPT,
  YOU CANNOT USE A HYPERLINK ELEMENT FOR THIS.
*/

// My incr() funcion
function incr() {
  var count = document.getElementById('counter');
  numCount = parseInt(count.innerHTML)
  numCount++;
  count.innerHTML = numCount;
  // google how to convert a string to an integer in JS
}

function decr() {
  var count = document.getElementById('counter');
  numCount = parseInt(count.innerHTML)
  if(numCount <= 0)
  {
    alert("You cannot have a value lower than 0.")
    return;
  }
  numCount--;
  count.innerHTML = numCount;
  // google how to convert a string to an integer in JS
}

function redir() {
  var redirBtn = document.getElementById('leave');
  document.location.href = 'https://www.codecademy.com/Brentboi';
  return;
  // how to redirect page via javascript
}
