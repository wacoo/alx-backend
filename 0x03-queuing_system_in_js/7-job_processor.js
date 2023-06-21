/* Create an array that will contain the blacklisted phone numbers.
Add in it 4153518780 and 4153518781 -these 2 numbers will be blacklisted
by our jobs processor.*/

import { createQueue } from 'kue';

const blacklist = ['4153518780', '4153518781'];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, function(job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
