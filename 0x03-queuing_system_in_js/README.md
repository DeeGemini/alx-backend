# 0x03. Queuing System in JS
`Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

Welcome to the `0x03. Queuing System in JS (JavaScript)` project. This
`README.md` will guide you through the setup, requirements and tasks involved
in building a `Redis` based queuing system using `Node.js`, `Express` and
`Kue`.
<br></br>

## Resources
### Read or watch:
- [Redis quick start](https://redis.io/docs/getting-started/)
- [Redis client interface](https://redis.io/topics/rediscli)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue (deprecated but still in use)](https://github.com/Automattic/kue)
<br></br>

## Learning Objectives
By the end of this project, you will be able to:
- Run a Redis server on your machine
- Perform basic Redis operations
- Use a Redis client with Node.js
- Store hash values in Redis
- Handle asynchronous operations with Redis
- Implement Kue as a queue system
- Build a basic Express app that interacts with Redis
- Create a basic Express app that interacts with Redis and a queue
<br></br>

## Requirements
- Code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A README.md file at the root of the project is mandatory
- Use `.js` extension for your code files
<br></br>

## Required Files
### `package.json`
This file is used to manage project dependencies and scripts.
```json
{
  "name": "queuing_system_in_js",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon --exec babel-node --presets @babel/preset-env"
  },
  "dependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "kue": "^0.11.6",
    "redis": "^3.1.2"
  }
}
```
<br></br>

### `.babelrc`
This file is used to configure Babel to use the `@babel/preset-env` preset.
```json
{
  "presets": ["@babel/preset-env"]
}
```
<br></br>

### Installation

Run the following command to install project dependencies:
```bash
$ npm install
```
<br></br>

---
## Author
- **Nontuthuzelo Ngwenya** - [GitHub](https://github.com/deegemini)
<br></br>

## License
None