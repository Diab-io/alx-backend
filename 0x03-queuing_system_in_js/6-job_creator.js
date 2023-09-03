import { createQueue } from "kue";
const queue =  createQueue();

const JobData = {
    phoneNumber: '74333',
    message: 'Hey, How are you',
};


const job = queue.create('push_notification_code', JobData).save((err) => {
    if (!err) console.log(`Notification job created: JOB ${job.id}`)
})

job.on('complete', () => console.log('Notification job completed'))

job.on('failed', () => console.log('Notification job failed'))
