/* use redis client to store hash */
import redis from 'redis';

const client = redis.createClient();

const hash = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

function storeHash() {
  for (const [key, val] of Object.entries(hash)) {
    client.hset('HolbertonSchools', key, val, redis.print);
  }
}

async function printHash() {
  await client.hgetall('HolbertonSchools', (err, res) => {
    console.log(res);
  });
}

storeHash();
printHash();
