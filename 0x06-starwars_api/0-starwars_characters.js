#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
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

getCharacters(process.argv[2]);
