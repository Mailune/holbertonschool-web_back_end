const readline = require('readline');

// Create an interface for input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Display the welcome message
console.log('Welcome to Holberton School, what is your name?');

// Listen for user input
rl.on('line', (input) => {
  // Display the user's name
  console.log(`Your name is: ${input}`);
  // Close the readline interface
  rl.close();
});

// When the interface closes, display the closing message
rl.on('close', () => {
  console.log('This important software is now closing');
});
