/* Create an array of jobs */
import { createQueue } from 'kue';

const blist = ['4153518780', '4153518781'];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blist.includes(phoneNumber)) {
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
