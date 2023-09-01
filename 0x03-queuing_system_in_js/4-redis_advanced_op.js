import { createClient, print } from "redis";
const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))

const setHash = (hashName, key, value) => {
    client.HSET(hashName, key, value, print)
}

const getHash = (hashName) => {
    client.HGETALL(hashName, (err, res) => console.log(res));
}

const main = () => {
    const hashData = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2
    }
    for (const [key, value] of Object.entries(hashData)) {
        setHash('cities', key, value);
    }
    getHash('cities');
}

client.on('connect', () => {
    console.log("Redis client connected to the server");
    main();
})
