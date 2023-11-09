# Star Wars API

This script retrieves and prints all characters from a specific Star Wars movie using the Star Wars API.

## Requirements

- Ubuntu 14.04 LTS
- Node.js version 10.14.x
- Editors: vi, vim, emacs
- Code style: Semistandard, with rules of Standard + semicolons on top and AirBnB style
- All files must be executable and end with a new line
- The first line of all files must be `#!/usr/bin/node`

## Installation

1. Clone the GitHub repository:

```bash
$ git clone https://github.com/ken-obieze/alx-interview.git
```

2. Navigate to the project directory:
```bash
$ cd alx-interview/0x06-starwars_api
```

3. Install the required dependencies:
```bash
$ sudo npm install request
$ sudo npm install semistandard
```

## Usage
Run the script by executing the following command:
```bash
$ ./0-starwars_characters.js <movie_id>
```
Replace <movie_id> with the desired movie ID. The script will retrieve and display the character names for the specified Star Wars movie.

## Example
To retrieve the characters from the movie "Return of the Jedi" (movie ID 3), run the following command:
```bash
$ ./0-starwars_characters.js 3
```
This will output the character names in the same order as the characters list in the API response.
