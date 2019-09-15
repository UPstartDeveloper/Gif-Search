var randomWords =
    ["books", "love", "family", "beach", "cartoon",
        "movies", "video games", "jelly beans", "sandwich", "string",
        "fruits", "building", "automobile", "ice cream", "mother",
        "journal", "imagination", "automation", "podcast", "dinner"];

// Inspired by https://scotch.io/tutorials/how-to-use-the-javascript-fetch-api-to-get-data
function getSuggestions(searchTerm){
const fetch = require("node-fetch");


fetch("http://suggestqueries.google.com/complete/search?q=" + searchTerm + "&client=safari").
    then((resp) => resp.json()).then(function(data){

    for (var index = 0; index < 10; index++){
        var result = JSON.stringify(data[1][index][0])
        result = result.substring(1, result.length - 1)
        console.log(result)
    }

})
}

getSuggestions('Potato') // testing getSuggestions
