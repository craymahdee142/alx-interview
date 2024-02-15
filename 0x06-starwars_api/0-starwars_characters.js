#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
