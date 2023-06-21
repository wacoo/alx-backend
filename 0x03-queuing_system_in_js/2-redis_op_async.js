/* Use promisify to modify the function displaySchoolValue to use async /await */

import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName, redis.print);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
