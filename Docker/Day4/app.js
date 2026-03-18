const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'db',   // container name
  user: 'root',
  password: 'root',
  database: 'testdb'
});

connection.connect(err => {
  if (err) {
    console.error('Error connecting:', err);
    return;
  }
  console.log('Connected to MySQL!');
});