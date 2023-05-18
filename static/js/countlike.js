function count(type) {
  const resultElement = document.getElementById('result');

  let number = resultElement.innerText;

  if(type == 'plus') {
    number = parseInt(number) + 1;
    }

resultElement.innerText = number;

}
