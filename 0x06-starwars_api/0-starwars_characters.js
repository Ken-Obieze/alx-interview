#!/usr/bin/node

// A script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/';

function getMovieCharacters (movieId) {
  const movieUrl = apiUrl + 'films/' + movieId + '/';
  request.get({ url: movieUrl }, function (error, response, body) {
    if (!error) {
      const characters = JSON.parse(body).characters;
      order(characters);
    }
  });
}

function order (characters) {
  if (characters.length > 0) {
    const characterUrl = characters.shift();
    request.get({ url: characterUrl }, function (error, response, body) {
      if (!error) {
        const character = JSON.parse(body).name;
        console.log(character);
        order(characters);
      }
    });
  }
}

getMovieCharacters(movieId);
