#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];
if (!movie_id  || isNaN(movie_id)) {
  process.exit(1);
}

function getCharacters(movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const film = JSON.parse(body);
      film.characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

getCharacters(movie_id);
