import { createClient } from "redis";
const client = createClient();

client.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

client.on('message', (channel, message) => {
    console.log(message)
    if (message === 'KILL_SERVER') {
        client.UNSUBSCRIBE(channel)
        client.QUIT()
    }
})

client.on('connect', () => {
    console.log('Redis client connected to the server');
    client.SUBSCRIBE('holberton school channel');
})
