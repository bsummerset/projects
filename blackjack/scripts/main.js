window.addEventListener('DOMContentLoaded', function() {
  // Execute after page load
})

let dealer = document.getElementById("dealer-hand");
let hand = document.getElementById("player-hand");
let button = document.getElementById("deal-button");
const suits = ["clubs", "diamonds", "hearts", "spades"]
const values = ["ace", 2,3,4,5,6,7,8,9,10,"jack", "queen","king"]

class Card{
  constructor(points, suit){
    this.points = points
    this.suit = suit
    this.imageUrl = '<img src = "images/' + points + '_of_' + suit + '.png">'
  }
}
let deck = [];
function buildDeck() {
  for(let i = 0; i <suits.length; i++){
    for(let x = 0; x <values.length; x++){
      deck.push (new Card(values[x],suits[i]));
 
    }
  }
}

buildDeck();
console.log(deck);
button.addEventListener("click", (e) =>{
  e.preventDefault()

  dealer.innerHTML = '<img src = "images/' + 2 + '_of_' + 'clubs' + '.png">'


})



// let card1 = values[Math.random(Math.random()*values.length)];
// let index1 = values.indexOf(card1);
// values.splice(index1,1);
// player.push(card1)

// let card2 = values[Math.random(Math.random()*cards.length)];
// let index2 = cards.indexOf(card2);
// cards.splice(index2,1);
// player.push(card2)

// let card3 = values[Math.random(Math.random()*cards.length)];
// let index3 = values.indexOf(card3);
// values.splice(index3,1);
// player.push(card3)

// let card4 = values[Math.random(Math.random()*cards.length)];
// let index4 = values.indexOf(card4);
// values.splice(index4,1);
// player.push(card4)

// for(let i = 0; i < player.length; i++){
//   player-points.push(player[i].value);
//   document.getElementById("player-hand").innerHTML += card;
// }
