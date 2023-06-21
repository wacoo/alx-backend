import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (_err, msg) => {
  console.log(msg)
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
