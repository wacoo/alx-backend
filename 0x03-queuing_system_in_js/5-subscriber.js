import redis from 'redis';

const client = redis.createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

client.subscribe('holberton school channel');

client.on('message', (err, msg) => {
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
