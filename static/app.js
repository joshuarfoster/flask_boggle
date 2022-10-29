
score = 0
$("#submit").click(async function(e) {
    e.preventDefault();
    guess = $('#guess').val();
    let response = await axios.get(`/check_valid_word?guess=${guess}`);
    $('h2').text(response.data.result);
    if (response.data.result === 'ok'){
        score = score + guess.length
        $('h3').text(`Score = ${score}`)  
    }
});
function endGame () {
    $('#submit').remove()
}
setTimeout(endGame,60000)