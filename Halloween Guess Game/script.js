const $ = function (id) {
  return document.getElementById(id)
}

const words = ['candy', 'ghost', 'mummy', 'pumpkin', 'spider', 'skeleton', 'vampire', 'zombie', 'witch'];
const images = ['images/candy.jpg', 'images/ghost.png', 'images/mummy2.jpg', 'images/pumpkinface.png', 'images/spider.jpg', 'images/skeleton.jpg', 'images/vampire.jpg', 'images/zombie.jpg', 'images/witch.jpg'];
let word
const img = document.createElement('img')
const parent = $('img')
let answerArray = []
let userGuess
let rightGuess = false
let userRightGuess = 0
let left = 9
let wins = 0
let losses = 0

function random () {
  const random = Math.floor(Math.random() * words.length)
  word = words[random]
  img.src = images[random]
}

function showBlank () {
  for (i = 0; i < word.length; i++) {
    answerArray[i] = '_'
  }
  $('guess').innerHTML = answerArray.join(' ')
}

function guessesLeft () {
  $('left').innerHTML = left
}

function winsScore () {
    $('wins').innerHTML = wins
}

function lossesScore () {
    $('losses').innerHTML = losses
}

function wrongGuess (char) {
    $('wrong').innerHTML += char + ', '
}

function initialGame () {
  if ($('winImage')) {
    $('winImage').remove()
  }
  left = 9
  answerArray = []
  $('wrong').innerHTML = ''
  userRightGuess = 0
  rightGuess = false
  guessesLeft()
  random()
  showBlank()
}

initialGame()
winsScore()
lossesScore()

function showLetter (char, str) {
  for (let j = 0; j < str.length; j++) {
    if (char === str[j]) {
      rightGuess = true
      answerArray.splice(j, 1, char)
      userRightGuess++
    }
  }
  $('guess').innerHTML = answerArray.join(' ')
}

let matchLength = function () {
  if (word.length === userRightGuess) return true
  else return false
}

document.onkeyup = function (event) {
  userGuess = event.key.toLowerCase();
  showLetter(userGuess, word)

  if (rightGuess) {
    rightGuess = false
    if (matchLength()) {
      const audio = new Audio('https://s3-us-west-2.amazonaws.com/s.cdpn.io/74196/win.mp3');
      audio.play()
      img.setAttribute('id', 'winImage')
      parent.appendChild(img)
      wins++
      winsScore()
      setTimeout(initialGame, 2000)
    } else {
    }
  } else {
    left--
    if (left < 1) {
      initialGame()
      losses++
      lossesScore()
    } else {
      wrongGuess(userGuess)
      guessesLeft()
    }
  }
}

// need to pick audio for incorrect letter and correct letter
// not just for when the game is won
// add a delay to view winning picture longer
// fix background header
