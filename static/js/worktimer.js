class Timer{

  constructor() {
    this.seconds = 00;
    this.minutes = 00;
    this.hours = 00;
    this.days = 00;
    this.appendSeconds = document.getElementById('seconds');
    this.appendMinutes = document.getElementById('minutes');
    this.appendHours = document.getElementById('hours');
    this.appendDays = document.getElementById('days');
  }

  startTime() {
    this.seconds++;

    if (this.seconds <= 9) {
      this.appendSeconds.innerHTML = '0' + this.seconds;
    }

    if (this.seconds > 9) {
      this.appendSeconds.innerHTML = this.seconds;
    }

    if (this.seconds >= 60) {
      this.minutes++;
      this.appendMinutes.innerHTML = '0' + this.minutes;
      this.seconds = 00;
      this.appendSeconds.innerHTML = '0' + this.seconds;
    }

    if (this.minutes >= 60) {
      this.hours++;
      this.appendHours.innerHTML = '0' + this.hours;
      this.minutes = 0;
      this.appendMinutes.innerHTML = '0' + this.minutes;
    }
  }




}
